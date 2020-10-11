import numpy as np
import random
import copy

from collapse_list import collapse_list

class Grid:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.grid = np.zeros((rows, columns))

    def value_at(self, row, column):
        return int(self.grid[row][column])

    def up(self):
        return self.collapse_up_down(is_reverse=False)

    def down(self):
        return self.collapse_up_down(is_reverse=True)

    def left(self):
        return self.collapse_left_right(is_reverse=False)

    def right(self):
        return self.collapse_left_right(is_reverse=True)

    def restart(self):
        self.grid = np.zeros((self.rows, self.columns))
        self.fill_random_cell()

    def get_free_cell_count(self):
        count = 0
        for c in range(self.columns):
            for r in range(self.rows):
                if self.grid[r][c] == 0:
                    count += 1
        return count

    def fill_random_cell(self):
        num_free_cells = self.get_free_cell_count()
        if num_free_cells == 0:
            return
        # Picks a random n between 0 and `num_free_cells`,
        # populates the nth free cell
        cell_number = random.randint(0, num_free_cells - 1)
        for c in range(self.columns):
            for r in range(self.rows):
                if self.grid[r][c] == 0:
                    if cell_number == 0:
                        self.grid[r][c] = 2
                        return
                    else:
                        cell_number -= 1

    def collapse_up_down(self, is_reverse):
        new_grid = copy.copy(self.grid)
        for c in range(self.columns):
            new_grid[:, c] = collapse_list(new_grid[:, c], is_reverse)
        if not np.array_equal(self.grid, new_grid):
            self.grid = new_grid # Only a valid move if board changes
            self.fill_random_cell()
            return True
        else:
            return False

    def collapse_left_right(self, is_reverse):
        new_grid = copy.copy(self.grid)
        for r in range(self.rows):
            new_grid[r] = collapse_list(new_grid[r], is_reverse)
        if not np.array_equal(self.grid, new_grid):
            self.grid = new_grid # Only a valid move if board changes
            self.fill_random_cell()
            return True
        else:
            return False
