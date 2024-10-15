class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        left = len(nums1) - m
        for _ in range(left):
            nums1.pop()

        for add in range(n):
            nums1.append(nums2[add])

        return sorted(nums1)


a = Solution()
print(a.merge(nums1=[0], m=0, nums2=[1], n=1))
