class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        n = len(nums1)
        m = len(nums2)
        mid1, mid2 = n // 2, m // 2
        if n % 2 == 0:
            med1 = (nums1[mid1 - 1] + nums1[mid1]) / 2
        else:
            med1 = nums1[mid1]

        if m % 2 == 0:
            med2 = (nums2[mid2 - 1] + nums2[mid2]) / 2
        else:
            med2 = nums2[mid2]
        return (med1 + med2) / 2


a = Solution()
print(a.findMedianSortedArrays(nums1=[1, 2], nums2=[3, 4]))
