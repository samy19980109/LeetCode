# Write a function that reverses a string.The input string is given as an array of characters char[].
#
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
#
# You may assume all the characters consist of printable ascii characters.
#
# Example 1:
#
# Input: ["h", "e", "l", "l", "o"]
# Output: ["o", "l", "l", "e", "h"]
#
# Example 2:
#
# Input: ["H", "a", "n", "n", "a", "h"]
# Output: ["h", "a", "n", "n", "a", "H"]

class Solution:
    '''
    start with two pointers, one on index 0 and the other one on index len(s) - 1 (last index)
    keeo swapping the values of the two pointers while left < right

    since we are not creating a lot of new variables, this is in O(1) space complexity

    and since we are not returning a new string, we are mutating the original string and therefore this is in-place
    '''
    def reverseString(self, s):
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left, right = left + 1, right - 1