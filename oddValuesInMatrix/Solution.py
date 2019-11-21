from typing import List


class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        rows_counter = set()
        cols_counter = set()
        for row, col in indices:
            if row in rows_counter:
                rows_counter.remove(row)
            else:
                rows_counter.add(row)
            if col in cols_counter:
                cols_counter.remove(col)
            else:
                cols_counter.add(col)
        odd_rows = len(rows_counter)
        odd_cols = len(cols_counter)
        return n * odd_cols + m * odd_rows - 2 * odd_cols * odd_rows


if __name__ == "__main__":
    print(Solution().oddCells(2, 2, [[1, 1], [0, 0]]))
