from math import gcd
from functools import reduce


class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        nums.sort()
        a = reduce(lambda x, y: gcd(x, y), numsDivide)
        for i in range(len(nums)):
            if a % nums[i] == 0:
                return i
        else:
            return -1
