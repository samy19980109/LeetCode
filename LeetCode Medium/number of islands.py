# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by
# water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges
# of the grid are all surrounded by water.
#
# Example 1:
#
# Input:
# 11110
# 11010
# 11000
# 00000
#
# Output: 1

# Example 2:
#
# Input:
# 11000
# 11000
# 00100
# 00011
#
# Output: 3

class Solution:
    '''
    this function just increments the count for the number of islands. In doing so it calls self.dfs
    '''
    def numIslands(self, grid):
        if not grid or len(grid) == 0:
            return 0

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1
        return count

    '''
    this is a helper function that makes the current element in the grid a '#' and also makes 
    the neighbouring elements in the grid a '#'. This ensures that if multiple '1' are together, then
    they should be counted as one big island. Therefore this prevents multicounting of the islands.  
    '''
    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
            return
        grid[i][j] = '#'
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i, j - 1)

# 11110
# 11010
# 11000
# 00000
test1 = [['1', '1', '1', '1', '0'], ['1', '1', '0', '1', '0'], ['1', '1', '0', '0', '0'], ['0', '0', '0', '0', '0']]
# 11000
# 11000
# 00100
# 00011
test2 = [['1', '1', '0', '0', '0'], ['1', '1', '0', '0', '0'], ['0', '0', '1', '0', '0'], ['0', '0', '0', '1', '1']]
x = Solution()
print(x.numIslands(test1))
print(x.numIslands(test2))