class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        length = rows * cols

        l = 0
        r = length - 1

        while l <= r:
            i = (l + r) // 2

            iPosition = self.digitToPosition(i, cols)
            curI = matrix[iPosition[0]][iPosition[1]]

            if curI == target:
                return True

            if curI < target:
                l = i + 1
            else:
                r = i - 1

        return False

    def digitToPosition(self, digit: int, cols: int):
        row = digit // cols
        col = digit % cols

        return (row, col)