class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        self = 0
        for nums in nums:
             self ^= nums
        return self