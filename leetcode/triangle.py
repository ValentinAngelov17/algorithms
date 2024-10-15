
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)
        minimum_sum = 0
        for i in range(n):
            minimum_sum += min(triangle[i])

        return minimum_sum


a = Solution()
print(a.minimumTotal(triangle=[[-10]]))
