class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check rows
        for i in range(9):
            seen = {}

            for j in range(9):
                num = board[i][j]

                if num == ".":
                    continue

                if num in seen:
                    return False

                seen[num] = 1

        # Check columns
        for j in range(9):
            seen = {}

            for i in range(9):
                num = board[i][j]

                if num == ".":
                    continue

                if num in seen:
                    return False

                seen[num] = 1

        # Check 3x3 boxes using your range idea
        start_row = 0
        start_col = 0

        while start_row < 9:

            seen = {}

            for i in range(start_row, start_row + 3):
                for j in range(start_col, start_col + 3):

                    num = board[i][j]

                    if num == ".":
                        continue

                    if num in seen:
                        return False

                    seen[num] = 1

            start_col += 3

            if start_col == 9:
                start_col = 0
                start_row += 3

        return True

        