class Solution:
    def majorityElement(self, nums: [int]) -> int:
        nums.sort()
        n = len(nums)
        print(nums[n // 2])


Solution().majorityElement([3,2,3])
