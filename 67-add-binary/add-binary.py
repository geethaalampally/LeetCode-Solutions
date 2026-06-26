class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) - 1
        j = len(b) - 1

        carry = 0
        res = ""

        while i >= 0 or j >= 0:
            b1 = int(a[i]) if i >= 0 else 0
            b2 = int(b[j]) if j >= 0 else 0

            digit = b1 ^ b2 ^ carry
            carry = (b1 & b2) | (b1 & carry) | (b2 & carry)

            res += str(digit)

            i -= 1
            j -= 1

        if carry:
            res += str(carry)

        return res[::-1]