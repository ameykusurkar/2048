import numpy as np
import random

ROWS, COLUMNS = 4, 4

class Grid:
    def __init__(self):
        self.grid = np.zeros((ROWS, COLUMNS))

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
