import numpy as np
import random
import copy

from collapse_list import collapse_list

ROWS, COLUMNS = 4, 4

class Grid:
    def __init__(self):
        self.grid = np.zeros((ROWS, COLUMNS))

    def up(self):
        return self.collapse_up_down(is_reverse=False)

    def down(self):
        return self.collapse_up_down(is_reverse=True)

    def left(self):
        return self.collapse_left_right(is_reverse=False)

    def right(self):
        return self.collapse_left_right(is_reverse=True)

    def restart(self):
        self.grid = np.zeros((ROWS, COLUMNS))
        start_r = random.randint(0, ROWS - 1)
        start_c = random.randint(0, COLUMNS - 1)
        self.grid[start_r][start_c] = 2

    def get_zeros(self):
        count = 0
        for c in range(COLUMNS):
            for r in range(ROWS):
                if self.grid[r][c] == 0:
                    count += 1
        return count

    def fill_random_cell(self):
        num_free_cells = self.get_zeros()
        if num_free_cells == 0:
            return
        cell_number = random.randint(0, num_free_cells - 1)
        for c in range(COLUMNS):
            for r in range(ROWS):
                if self.grid[r][c] == 0:
                    if cell_number == 0:
                        self.grid[r][c] = 2
                        return
                    cell_number -= 1

    def collapse_up_down(self, is_reverse):
        new_grid = copy.copy(self.grid)
        for c in range(COLUMNS):
            new_grid[:, c] = collapse_list(new_grid[:, c], is_reverse)
        if not np.array_equal(self.grid, new_grid):
            self.grid = new_grid # Only a valid move if board changes
            self.fill_random_cell()
            return True
        else:
            return False

    def collapse_left_right(self, is_reverse):
        new_grid = copy.copy(self.grid)
        for r in range(ROWS):
            new_grid[r] = collapse_list(new_grid[r], is_reverse)
        if not np.array_equal(self.grid, new_grid):
            self.grid = new_grid # Only a valid move if board changes
            self.fill_random_cell()
            return True
        else:
            return False
