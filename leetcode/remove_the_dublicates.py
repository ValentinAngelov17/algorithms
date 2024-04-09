class Solution:
    def removeDuplicates(self, nums: [int]) -> int:
        without_dublicates = set(nums)
        print(len(without_dublicates))

Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4])