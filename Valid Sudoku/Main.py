from typing import List, Optional 

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(input)):
            seenRow = set()
            for j in range(len(input[i])):
                if input[i][j] == ".":
                    continue
                if input[i][j] in seenRow:
                    return False
                seenRow.add(input[i][j])
        
        for i in range(len(input)):
            seenCol = set()
            for j in range(len(input[i])):
                if input[j][i] == ".":
                    continue
                if input[j][i] in seenCol:
                    return False
                seenCol.add(input[j][i])

        for square in range(9):
            seenSquare = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seenSquare:
                        return False
                    seenSquare.add(board[row][col])
        return True

if __name__ == "__main__":
    solution = Solution()
    input = [["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]

    print(solution.isValidSudoku(input))