class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        neighbors = []
        final_board = {}
        steps = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]

        for rows in range(len(board)):
            for columns in range(len(board[0])):
                element = board[rows][columns]
                neighbors = []
                for step in steps:
                    row = rows + step[0]
                    column = columns + step[1]
                    if row < 0 or (row > len(board) - 1) or column < 0 or (column > len(board[0]) - 1):
                        continue
                    else:
                        neighbors.append(board[row][column])

                live_count = neighbors.count(1)
                if element == 1:
                    if live_count < 2:
                        final_board[(rows, columns)] = 0
                    elif live_count > 3:
                        final_board[(rows, columns)] = 0
                else:
                    if live_count == 3:
                        final_board[(rows, columns)] = 1

        for key, value in final_board.items():
            row, col = key
            board[row][col] = value
        return board


a = Solution()
print(a.gameOfLife([[1,1],[1,0]]))
