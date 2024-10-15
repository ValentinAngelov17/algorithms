class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        result = []
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    current = sorted([nums[i], nums[j], nums[k]])
                    if sum(current) == 0 and current not in result:
                        result.append(current)

        return result


a = Solution()
print(a.threeSum(nums=[1,-1,-1,0]))
