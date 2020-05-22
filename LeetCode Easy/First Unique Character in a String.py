# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
#
# Examples:
#
# s = "leetcode"
# return 0.
#
# s = "loveleetcode",
# return 2.

class Solution:
    def firstUniqChar(self, s: str) -> int:
        letters = 'abcdefghijklmnopqrstuvwxyz'
        # make a list of all the inndex in s such that the count of the letter in s is 1
        index = [s.index(l) for l in letters if s.count(l) == 1]
        # return the minimum of the list of index, thereby returning the first index which is non repeating
        return min(index) if len(index) > 0 else -1
