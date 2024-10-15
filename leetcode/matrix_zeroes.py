
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        b = len(matrix[0])
        c = len(matrix)
        zero_indexes = []

        for rows in range(c):
            for column in range(b):
                if matrix[rows][column] == 0:
                    zero = (rows, column)
                    zero_indexes.append(zero)

        for zero in zero_indexes:
            row_index = zero[0]
            col_index = zero[1]
            matrix[row_index] = [0] * b
            for row in range(c):
                matrix[row][col_index] = 0

        return matrix


a = Solution()
print(a.setZeroes(matrix = [[1,1,2,1],[3,4,5,2],[1,3,1,5]]))
