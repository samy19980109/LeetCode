#Given an integer, write a function to determine if it is a power of two.
#
# Example 1:
#
# Input: 1
# Output: true
# Explanation: 20 = 1
# Example 2:
#
# Input: 16
# Output: true
# Explanation: 24 = 16
# Example 3:
#
# Input: 218
# Output: false

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        i = 1
        while(i < n):
            i *= 2

        return i == n

    def isPowerOfTwo2(self, n):
        """
        n & n - 1 removes the left most bit of n. If an integer is power of 2, there is a single bit in the
        binary representation of n. e.g. 16 = b10000, 16 - 1 = b01111, and 16 & 16 - 1 = b10000 & b01111 = 0,
        also 16 != 0, based on these facts there is only one bit in b10000, so 16 is power of 2.
        :type n: int
        :rtype: bool
        """
        return n > 0 and not (n & n - 1)

x = Solution()
print(x.isPowerOfTwo(256))