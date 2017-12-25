import tkinter as tk
import numpy as np
import random

from collapse_list import collapse_list

root = tk.Tk()
root.wm_title("2048")

ROWS, COLUMNS = 4, 4
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

grid = np.zeros((ROWS, COLUMNS))
display = []

def restart():
  global grid
  grid = np.zeros((ROWS, COLUMNS))
  start_r = random.randint(0, ROWS - 1)
  start_c = random.randint(0, COLUMNS - 1)
  grid[start_r][start_c] = 2
  display_grid()

def display_grid():
  for r in range(ROWS):
    for c in range(COLUMNS):
      display_text, display_colour = str(int(grid[r][c])), ''
      if grid[r][c] == 0:
        display_text, display_colour = '', '#C0C0C0'
      display_colour = TILE_COLOURS.get(grid[r][c], 'black')
      display[r][c].config(text=display_text)
      display[r][c].config(bg=display_colour)

def collapse_up_down(event):
  # Check if Up or Down key
  is_reverse = (event.char == '\uf701')
  for c in range(COLUMNS):
      grid[:, c] = collapse_list(grid[:, c], is_reverse)
  fill_random_cell(get_zeros())
  display_grid()
      
def collapse_left_right(event):
  # Check if Left or Right key
  is_reverse = (event.char == '\uf703')
  for r in range(ROWS):
      grid[r] = collapse_list(grid[r], is_reverse)
  fill_random_cell(get_zeros())
  display_grid()
      
def get_zeros():
  count = 0
  for c in range(COLUMNS):
    for r in range(ROWS):
      if grid[r][c] == 0:
        count += 1
  return count
      
def fill_random_cell(num_free_cells):
  if num_free_cells == 0:
    return
  cell_number = random.randint(0, num_free_cells - 1)
  for c in range(COLUMNS):
    for r in range(ROWS):
      if grid[r][c] == 0:
        if cell_number == 0:
          grid[r][c] = 2
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
grid[start_r][start_c] = 2
display_grid()
root.mainloop()
