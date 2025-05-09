class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if len(points) < 3:
            return len(points)

        dict = {}
        for b in points:
            for a in points:
                if a == b:
                    continue

                k = a[0] - b[0]
                if k == 0:
                    f = (a[0],)
                else:
                    ax = (a[1] - b[1]) / k
                    bb = (a[0] * b[1] - a[1] * b[0]) / k
                    f = (ax, bb)

                if f not in dict:
                    dict[f] = set()
                dict[f].add(tuple(a))

        return max(len(v) for k, v in dict.items())





a = Solution()
print(a.maxPoints(points=[[1, 1], [2, 2], [3, 3]]))
