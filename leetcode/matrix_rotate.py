class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        dublicate_matrix = []
        for row in range(rows):
            new_row = []
            for col in range(cols - 1, -1, -1):
                new_row.append(matrix[col][row])
            dublicate_matrix.append(new_row)

        for row in range(rows):
            matrix[row] = dublicate_matrix[row]

        return matrix


a = Solution()
print(a.rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
