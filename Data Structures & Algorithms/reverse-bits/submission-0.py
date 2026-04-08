class Solution:
    def reverseBits(self, n: int) -> int:
        self = 0
        for _ in range(32):
            self = (self << 1) | (n & 1)
            n >>= 1
        return self