
class SudokuSolver:
    def solve(self, board):
        empty_position = self.find_empty_position(board)
        if not empty_position:
            return True
        row, col = empty_position

        for num in range(1, 10):
            if self.is_safe(board, row, col, num):
                board[row][col] = num
                if self.solve(board):
                    return True
                board[row][col] = 0

        return False

    def find_empty_position(self, board):
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:
                    return row, col
        return None

    def is_safe(self, board, row, col, num):
        for i in range(9):
            if board[row][i] == num or board[i][col] == num:
                return False
        
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board[i][j] == num:
                    return False
        
        return True

    def validate(self, board):
        # Validate rows
        for row in board:
            if not self.is_valid_set(row):
                return False
        
        # Validate columns
        for col in range(9):
            if not self.is_valid_set([row[col] for row in board]):
                return False
        
        # Validate subgrids
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                subgrid = [board[x][y] for x in range(i, i+3) for y in range(j, j+3)]
                if not self.is_valid_set(subgrid):
                    return False
        
        return True

    def is_valid_set(self, nums):
        nums_set = {num for num in nums if num != 0}
        return len(nums_set) == len([num for num in nums if num != 0])
