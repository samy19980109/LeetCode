# https://leetcode.com/problems/rotting-oranges/
#
# In a given grid, each cell can have one of three values:
#
# - the value 0 representing an empty cell;
# - the value 1 representing a fresh orange;
# - the value 2 representing a rotten orange.
#
# Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.
#
# Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.
#
# Example 1:
# Input: [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
#
# Example 2:
# Input: [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
#
# Example 3:
# Input: [[0,2]]
# Output: 0
# Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.

class Solution:
    def orangesRotting(self, grid) -> int:
        row, col = len(grid), len(grid[0])
        # make a list of all the rotting oranges
        rotting = {(i, j) for i in range(row) for j in range(col) if grid[i][j] == 2}
        # make a list of all the fresh oranges
        fresh = {(i, j) for i in range(row) for j in range(col) if grid[i][j] == 1}
        timer = 0
        while fresh:
            if not rotting: return -1
            # for all the adjacent oranges in fresh, make them rot when one timer goes by
            rotting = {(i+di, j+dj) for i, j in rotting for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)] if (i+di, j+dj) in fresh}
            # update fresh so that the oranges next to the rotten ones are no longer in fresh
            fresh -= rotting
            timer += 1
        return timer