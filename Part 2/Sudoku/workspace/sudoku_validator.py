
class SudokuValidator:
    def validate(self, board):
        return (self.check_rows(board) and 
                self.check_columns(board) and 
                self.check_squares(board))

    def check_rows(self, board):
        for row in board:
            nums = [num for num in row if num != 0]
            if len(nums) != len(set(nums)):
                return False
        return True

    def check_columns(self, board):
        for col in range(9):
            nums = [board[row][col] for row in range(9) if board[row][col] != 0]
            if len(nums) != len(set(nums)):
                return False
        return True

    def check_squares(self, board):
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                nums = [board[x][y] for x in range(i, i+3) for y in range(j, j+3) if board[x][y] != 0]
                if len(nums) != len(set(nums)):
                    return False
        return True
