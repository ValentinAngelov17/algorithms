class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        Input: s = "PAYPALISHIRING", numRows = 4
        Output: "PINALSIGYAHRPI"
        Explanation:
        P     I    N
        A   L S  I G
        Y A   H R
        P     I
        00        03      06
        10     12 13   15 16
        20 21     23 24   26
        30        33
        """
        matrix = []
        for i in range(numRows):
            matrix.append("")

        row_counter = 0
        is_reverse = False

        for char in s:
            if numRows == 1:
                return s
            matrix[row_counter] += char
            if is_reverse:
                row_counter -= 1
            else:
                row_counter += 1

            if row_counter == (numRows - 1):
                is_reverse = True
            elif row_counter == 0:
                is_reverse = False

        return "".join(matrix)


a = Solution()
print(a.convert("AB", 1))
