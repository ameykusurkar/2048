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
  startR = random.randint(0, ROWS - 1)
  startC = random.randint(0, COLUMNS - 1)
  grid[startR][startC] = 2
  displayGrid()

F = tk.Frame(root, height=500, width=500, bg='#606060')
B = tk.Button(root, text="Restart", command=restart)

# Setting up grid and display
for r in range(ROWS):
  displayRow = []
  for c in range(COLUMNS):
    newLabel = tk.Label(F, bg='#E74C3C', fg='white',
                     borderwidth=10, 
                     width = 4, height = 2,
                     font=("Arial", 28))
    newLabel.grid(row=r,column=c, padx=3, pady=3)
    displayRow.append(newLabel)
  display.append(displayRow)

def displayGrid():
  for r in range(ROWS):
    for c in range(COLUMNS):
      displayText, displayColour = str(int(grid[r][c])), ''
      if grid[r][c] == 0:
        displayText, displayColour = '', '#C0C0C0'
      displayColour = TILE_COLOURS.get(grid[r][c], 'black')
      display[r][c].config(text=displayText)
      display[r][c].config(bg=displayColour)

def collapseUp(event):
  for c in range(COLUMNS):
      grid[:, c] = collapse_list(grid[:, c])
  fillRandomCell(getZeros())
  displayGrid()
      
def collapseDown(event):
  for c in range(COLUMNS):
      grid[:, c] = collapse_list(grid[:, c], reverse=True)
  fillRandomCell(getZeros())
  displayGrid()
      
def collapseLeft(event):
  for r in range(ROWS):
      grid[r] = collapse_list(grid[r])
  fillRandomCell(getZeros())
  displayGrid()
      
def collapseRight(event):
  for r in range(ROWS):
      grid[r] = collapse_list(grid[r], reverse=True)
  fillRandomCell(getZeros())
  displayGrid()
      
def getZeros():
  count = 0
  for c in range(COLUMNS):
    for r in range(ROWS):
      if grid[r][c] == 0:
        count += 1
  return count
      
def fillRandomCell(numFreeCells):
  if numFreeCells == 0:
    return
  cellNumber = random.randint(0, numFreeCells - 1)
  for c in range(COLUMNS):
    for r in range(ROWS):
      if grid[r][c] == 0:
        if cellNumber == 0:
          grid[r][c] = 2
          return
        cellNumber -= 1

F.pack()
B.pack()

root.bind('<Up>', collapseUp)
root.bind('<Down>', collapseDown)
root.bind('<Left>', collapseLeft)
root.bind('<Right>', collapseRight)

startR = random.randint(0, ROWS - 1)
startC = random.randint(0, COLUMNS - 1)
grid[startR][startC] = 2
displayGrid()
root.mainloop()
