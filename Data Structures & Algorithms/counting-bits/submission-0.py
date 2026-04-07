class Solution:
    def countBits(self, n: int) -> List[int]:
        self = [0] * (n + 1)
        for i in range(1, n+1):
            self[i] =  self[i//2] + i % 2
        return self