class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        first_number = max(nums)
        left = target - first_number
        subarray = []
        while sum(subarray) < target:
            pass


a = Solution()
print(Solution.minSubArrayLen(target=7, nums=[2, 3, 1, 2, 4, 3]))
