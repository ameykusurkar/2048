import random

from collapse_list import collapse_list


class Grid:
    def __init__(self, rows: int, columns: int) -> None:
        self.rows = rows
        self.columns = columns
        self.grid: list[list[int]] = [[0] * columns for _ in range(rows)]

    def value_at(self, row: int, column: int) -> int:
        return self.grid[row][column]

    def up(self) -> bool:
        return self._collapse(axis="column", reverse=False)

    def down(self) -> bool:
        return self._collapse(axis="column", reverse=True)

    def left(self) -> bool:
        return self._collapse(axis="row", reverse=False)

    def right(self) -> bool:
        return self._collapse(axis="row", reverse=True)

    def restart(self) -> None:
        self.grid = [[0] * self.columns for _ in range(self.rows)]
        self._fill_random_cell()

    def _collapse(self, axis: str, reverse: bool) -> bool:
        old_grid = [row[:] for row in self.grid]

        if axis == "row":
            for r in range(self.rows):
                self.grid[r] = collapse_list(self.grid[r], reverse)
        else:
            for c in range(self.columns):
                col = [self.grid[r][c] for r in range(self.rows)]
                collapsed = collapse_list(col, reverse)
                for r in range(self.rows):
                    self.grid[r][c] = collapsed[r]

        if self.grid != old_grid:
            self._fill_random_cell()
            return True
        return False

    def _fill_random_cell(self) -> None:
        free_cells = [
            (r, c)
            for r in range(self.rows)
            for c in range(self.columns)
            if self.grid[r][c] == 0
        ]
        if free_cells:
            r, c = random.choice(free_cells)
            self.grid[r][c] = 2
