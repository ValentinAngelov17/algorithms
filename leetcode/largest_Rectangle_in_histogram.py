class Solution:
    def largestRectangleArea(self, heights):
        largest_area = 0
        current_minimum = heights[0]
        index = 0
        for i in range(len(heights)):
            if heights[i] < current_minimum:
                current_minimum = heights[i]
                index = i + 1
            largest_area = max(largest_area, heights[i] * (i - index))


        return largest_area


a = Solution()
print(a.largestRectangleArea(heights=[1, 3, 7]))
