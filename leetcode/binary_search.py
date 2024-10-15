class Solution:
    def search(self, nums: list[int], target: int):
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                return m
        return -1


a = Solution()
print(a.search(nums=[-1, 0, 2, 3, 4, 8], target=4))
