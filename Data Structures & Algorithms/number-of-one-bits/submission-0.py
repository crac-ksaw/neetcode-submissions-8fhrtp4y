class Solution:
    def hammingWeight(self, n: int) -> int:
        self = 0
        while n:
            n = n & (n-1)
            self += 1
        return self