# Given a non-empty array of integers, every element appears twice except for one. Find that single one.
#
# Note:
#
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
#
# Example 1:
#
# Input: [2,2,1]
# Output: 1
# Example 2:
#
# Input: [4,1,2,1,2]
# Output: 4

class Solution:
    def singleNumber(self, nums) -> int:
        hash_table = {}
        for i in nums:
            if i in hash_table:
                hash_table[i] += 1
            else:
                hash_table[i] = 1

        for i in hash_table:
            if hash_table[i] == 1:
                return i

    '''
    Concept:

    If we take XOR of zero and some bit, it will return that bit
    a XOR 0 = a XOR 0 = a
        
    If we take XOR of two same bits, it will return 0
    a XOR a = a XOR a = 0
    a XOR b XOR a = (a XOR a) XOR b = 0 XOR b = a XOR b XOR a=(a XOR a) XOR b=0 XOR b = b
    So we can XOR all bits together to find the unique number.
    '''
    def singleNumber2(self, nums) -> int:
        a = 0
        for i in nums:
            a ^= i
        return a