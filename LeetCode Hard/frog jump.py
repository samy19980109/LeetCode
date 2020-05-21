# A frog is crossing a river. The river is divided into x units and at each unit there may or may not exist a stone. The frog can jump on a stone, but it must not jump into the water.
#
# Given a list of stones' positions (in units) in sorted ascending order, determine if the frog is able to cross the river by landing on the last stone. Initially, the frog is on the first stone and assume the first jump must be 1 unit.
#
# If the frog's last jump was k units, then its next jump must be either k - 1, k, or k + 1 units. Note that the frog can only jump in the forward direction.
#
# Note:
#
# The number of stones is ≥ 2 and is < 1,100.
# Each stone's position will be a non-negative integer < 231.
# The first stone's position is always 0.

# Example 1:
#
# [0,1,3,5,6,8,12,17]
#
# There are a total of 8 stones.
# The first stone at the 0th unit, second stone at the 1st unit,
# third stone at the 3rd unit, and so on...
# The last stone at the 17th unit.
#
# Return true. The frog can jump to the last stone by jumping
# 1 unit to the 2nd stone, then 2 units to the 3rd stone, then
# 2 units to the 4th stone, then 3 units to the 6th stone,
# 4 units to the 7th stone, and 5 units to the 8th stone.

# Example 2:
#
# [0,1,2,3,4,8,9,11]
#
# Return false. There is no way to jump to the last stone as
# the gap between the 5th and 6th stone is too large.

class Solution:
    '''
    first if statement if error checking

    dp is all the positions of the stone
    stack includes all the positions and add the jumps
    visited all the previous stone positions we have visited and how we reached there

    if we reach the last stone, then we have succeeded and we are done

    otherwise we make a jumo of either previous jump - 1, previous jump or previous jump + 1
    and if we land on a new stone which is greater than the current position (cause we want to move forward)
    and we havent visited that stone before, then we add that stone to the stack as well as visited list.

    If by the end of the loop, we havent reached the final stone, then we have exhausted all the possibilities
    and there is no way
    '''
    def canCross(self, stones: List[int]) -> bool:
        if len(stones) < 2 or stones[1] != 1:
            return False
        dp = {x for x in stones}
        stack = [(1, 1)]
        visited = {(1, 1)}
        while stack:
            cur_pos, prev_k = stack.pop()
            if cur_pos == stones[-1]:
                return True
            for k in range(-1, 2):
                new_k = prev_k + k
                new_pos = cur_pos + new_k
                if new_pos > cur_pos and new_pos in dp and (new_pos, new_k) not in visited:
                    visited.add((new_pos, new_k))
                    stack.append((new_pos, new_k))
        return False