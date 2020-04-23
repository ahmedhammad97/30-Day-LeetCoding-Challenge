class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        result = 0
        while m != n:
            m >>= 1
            n >>= 1
            result += 1
        return n << result


# The bitwise AND is keeping the common bits
#  of m and n from left to right until the first
#  bit that they are different, padding zeros
#  for the rest.