class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowList = [{} for _ in range(len(board))]
        colList = [{} for _ in range(len(board))]
        gridList = [{} for _ in range(9)]

        for row in range(len(board)):
            for col in range(len(board[0])):
                num = board[row][col]
                if num == ".":
                    continue
                #check row
                if num not in rowList[row]:
                    rowList[row][num] = 1
                else: return False

                #check col
                if num not in colList[col]:
                    colList[col][num] = 1
                else: return False

                #check grid
                grid = (row // 3) * 3 + (col // 3)
                if num not in gridList[grid]:
                    gridList[grid][num] = 1
                else: return False

        return True
