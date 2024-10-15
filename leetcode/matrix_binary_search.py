class Solution:
    def searchMatrix(self, matrix, target):
        row = 0
        for i in range(len(matrix)):
            if matrix[i][-1] >= target:
                row = i
                break
        l, r = 0, len(matrix[row]) - 1
        while l <= r:
            m = (l + r) // 2
            if matrix[row][m] < target:
                l = m + 1
            elif matrix[row][m] > target:
                r = m - 1
            else:
                return True
        return False


a = Solution()
print(a.searchMatrix([[1], [3]], target=1))
st = (1,2,3,4,5,6,7,8,9,2)

print(st)
s = "abff"
b = s.count(s)
print(b)