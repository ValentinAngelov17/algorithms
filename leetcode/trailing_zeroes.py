import math


class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        c = 0
        while n >= 5:
            n //= 5
            c += n

        return c


a = Solution()
print(a.trailingZeroes(n=7))
