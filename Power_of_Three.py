# Power of Three

import math

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        return (math.log10(n) / math.log10(3)) % 1 == 0
