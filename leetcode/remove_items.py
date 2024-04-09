class Solution:
    def removeElement(self, nums: [int], val: int) -> int:
        counter = 0
        while val in nums:
            if val in nums:
                nums.remove(val)
                nums.append("_")
                counter += 1
        print(len(nums) - counter,", ", nums)


Solution().removeElement(nums=[3, 2, 2, 3], val=3)
