class Solution:
    def merge(self, nums1: [], m: int, nums2: [], n: int):
        merge_list = nums1[0:m] + nums2[0:n]
        nums1 = merge_list
        print(nums1)


Solution().merge([0], 0, [1], 1)