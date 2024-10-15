import time


class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        minutes = []
        for time in timePoints:
            h, m = map(int, time.split(':'))
            minutes.append(h * 60 + m)

        minutes.sort()

        min_diff = float('inf')
        for i in range(len(minutes) - 1):
            min_diff = min(min_diff, minutes[i + 1] - minutes[i])

        min_diff = min(min_diff, 24 * 60 - minutes[-1] + minutes[0])

        return min_diff


a = Solution()
print(a.findMinDifference(timePoints=["23:59", "00:00"]))
