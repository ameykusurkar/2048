import tkinter as tk
import numpy as np
import copy
import random

from grid import Grid, ROWS, COLUMNS
from collapse_list import collapse_list

root = tk.Tk()
root.wm_title("2048")

TILE_COLOURS = {
    0:    '#C0C0C0',
    2:    '#1ABC9C',
    4:    '#16A085',
    8:    '#2ECC71',
    16:   '#27AE60',
    32:   '#3498DB',
    64:   '#2980B9',
    128:  '#34495E',
    256:  '#2C3E50',
    512:  '#EA4C88',
    1024: '#CA2C68',
}

grid = Grid()
display = []

def restart():
    grid.restart()
    display_grid()

def display_grid():
  for r in range(ROWS):
    for c in range(COLUMNS):
      display_text, display_colour = str(int(grid.grid[r][c])), ''
      if grid.grid[r][c] == 0:
        display_text, display_colour = '', '#C0C0C0'
      display_colour = TILE_COLOURS.get(grid.grid[r][c], 'black')
      display[r][c].config(text=display_text)
      display[r][c].config(bg=display_colour)

def collapse_up_down(event):
  # Check if Up or Down key
  is_reverse = (event.char == '\uf701')
  global grid
  new_grid = copy.copy(grid.grid)
  for c in range(COLUMNS):
      new_grid[:, c] = collapse_list(new_grid[:, c], is_reverse)
  if not np.array_equal(grid.grid, new_grid):
      grid.grid = new_grid # Only a valid move if board changes
      fill_random_cell()
      display_grid()

def collapse_left_right(event):
  # Check if Left or Right key
  is_reverse = (event.char == '\uf703')
  global grid
  new_grid = copy.copy(grid.grid)
  for r in range(ROWS):
      new_grid[r] = collapse_list(new_grid[r], is_reverse)
  if not np.array_equal(grid.grid, new_grid):
      grid.grid = new_grid # Only a valid move if board changes
      fill_random_cell()
      display_grid()

def fill_random_cell():
    num_free_cells = grid.get_zeros()
    if num_free_cells == 0:
        return
    cell_number = random.randint(0, num_free_cells - 1)
    for c in range(COLUMNS):
        for r in range(ROWS):
            if grid.grid[r][c] == 0:
                if cell_number == 0:
                    grid.grid[r][c] = 2
                    return
                cell_number -= 1

##### GUI and Game setup #####

F = tk.Frame(root, height=500, width=500, bg='#606060')
B = tk.Button(root, text="Restart", command=restart)

for r in range(ROWS):
  display_row = []
  for c in range(COLUMNS):
    new_label = tk.Label(F, bg='#E74C3C', fg='white',
                         borderwidth=10,
                         width=4, height=2,
                         font=("Arial", 28))
    new_label.grid(row=r,column=c, padx=3, pady=3)
    display_row.append(new_label)
  display.append(display_row)

F.pack()
B.pack()

root.bind('<Up>', collapse_up_down)
root.bind('<Down>', collapse_up_down)
root.bind('<Left>', collapse_left_right)
root.bind('<Right>', collapse_left_right)

start_r = random.randint(0, ROWS - 1)
start_c = random.randint(0, COLUMNS - 1)
grid.grid[start_r][start_c] = 2
display_grid()
root.mainloop()
