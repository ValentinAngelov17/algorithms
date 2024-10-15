from collections import defaultdict


class Solution(object):
    def isValidSudoku(self, board):
        column = defaultdict(set)
        row = defaultdict(set)
        box = defaultdict(set)
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".": continue
                if board[i][j] in column[i] or board[i][j] in row[j] or board[i][j] in box[(i // 3, j // 3)]:
                    return False

                column[i].add(board[i][j])
                row[j].add(board[i][j])
                box[(i // 3, j // 3)].add(board[i][j])
        return True


a = Solution()
print(a.isValidSudoku(board=
                      [["8", "3", ".", ".", "7", ".", ".", ".", "."]
                          , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
                          , [".", "9", "8", ".", ".", ".", ".", "6", "."]
                          , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
                          , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
                          , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
                          , [".", "6", ".", ".", ".", ".", "2", "8", "."]
                          , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
                          , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
