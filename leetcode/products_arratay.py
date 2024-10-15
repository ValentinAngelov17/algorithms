class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        result = []
        diff = len(nums)
        for i in range(diff):
            number = nums[i]
            temp = 1
            something = [temp * x for x in nums[i:]]
            result.append(something)
        return result

a = Solution()
print(a.productExceptSelf(nums=[-1, 0, 1, 2, 3]))
