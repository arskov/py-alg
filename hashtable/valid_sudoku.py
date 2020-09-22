from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(3):
            for j in range(3):
                square_dict = set()
                for k in range(3):
                    for l in range(3):
                        square_val = board[i*3 + k][j*3 + l]
                        if square_val != "." and square_val in square_dict:
                            return False
                        square_dict.add(square_val)
        for i in range(9):
            row_dict = set()
            col_dict = set()
            for j in range(9):
                row_val = board[i][j]
                col_val = board[j][i]
                if row_val != "." and row_val in row_dict:
                    return False
                row_dict.add(row_val)
                if col_val != "." and col_val in col_dict:
                    return False
                col_dict.add(col_val)
        return True

if __name__ == "__main__":
    sol = Solution()
    sudoku1 = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    print(sol.isValidSudoku(sudoku1))
    sudoku2 = [
        ["8","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    print(sol.isValidSudoku(sudoku2))
