class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        width = len(nums)
        operations = 0
        step = nums[1]
        while True:
            nums[step]





a = Solution()
print(a.canJump(nums=[2, 3, 1, 1, 4]))
