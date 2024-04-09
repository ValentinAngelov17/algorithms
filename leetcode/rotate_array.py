class Solution:
    def rotate(self, nums: list, k: int) -> None:
        left = len(nums) - k
        for i in range(left):
            number = nums.pop(0)
            nums.append(number)
        print(nums)

Solution().rotate(nums = [1,2,3,4,5,6,7], k = 3)