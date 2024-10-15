class Solution:
    def trap(self, height: list[int]) -> int:
        if not height:
            return 0

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                leftMax = max(rightMax, height[r])
                res += rightMax - height[r]

        return res


a = Solution()
print(a.trap(height=[0, 2, 0, 3, 1, 0, 1, 3, 2, 1]))
