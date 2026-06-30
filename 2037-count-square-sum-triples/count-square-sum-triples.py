import math

class Solution:
    def countTriples(self, n: int) -> int:
        res = 0

        for a in range(1, n + 1):
            for b in range(1, n + 1):
                c2 = a*a + b*b
                c = math.isqrt(c2)   # integer square root

                if c*c == c2 and c <= n:
                    res += 1

        return res