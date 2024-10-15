import sys


class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)
        min_length = sys.maxsize
        for i in range(n - target + 1):
            current_sum = 0
            for j in range(target):
                current_sum = current_sum + nums[i + j]
                if current_sum >= target:
                    check = len(nums[i:i + j + 1])
                    if check < min_length:
                        min_length = check
        if min_length == sys.maxsize:
            return 0
        else:
            return min_length


a = Solution()
print(a.minSubArrayLen(target=11, nums=[1, 2, 3, 4, 5]))
