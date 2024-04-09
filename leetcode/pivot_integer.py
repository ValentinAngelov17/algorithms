import math


class Solution:
    def pivotInteger(self, n: int) -> int:
        a = [x for x in range(1, n + 1)]
        b = 0
        while a:
            list1 = sum(a)
            list2 = a.pop()
            b += list2
            if list1 == b:
                return list2
        return -1



print(Solution().pivotInteger(4))
