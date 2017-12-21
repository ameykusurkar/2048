import tkinter as tk
import numpy as np
import random

root = tk.Tk()
root.wm_title("2048")

ROWS, COLUMNS = 4, 4

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
      elif grid[r][c] == 2:
        displayColour = '#1ABC9C'
      elif grid[r][c] == 4:
        displayColour = '#16A085'
      elif grid[r][c] == 8:
        displayColour = '#2ECC71'
      elif grid[r][c] == 16:
        displayColour = '#27AE60'
      elif grid[r][c] == 32:
        displayColour = '#3498DB'
      elif grid[r][c] == 64:
        displayColour = '#2980B9'
      elif grid[r][c] == 128:
        displayColour = '#34495E'
      elif grid[r][c] == 256:
        displayColour = '#2C3E50'
      elif grid[r][c] == 512:
        displayColour = '#EA4C88'
      elif grid[r][c] == 1024:
        displayColour = '#CA2C68'
      else:
        displayColour = 'black'
      display[r][c].config(text=displayText)
      display[r][c].config(bg=displayColour)

def collapseUp(event):
  flushBefore = flushUp()
  for c in range(COLUMNS):
    for r in range(ROWS-1):
      if grid[r][c] == grid[r+1][c]:
        grid[r][c] += grid[r+1][c]
        grid[r+1][c] = 0
  flushAfter = flushUp()
  if not (flushBefore or flushAfter):
    # No move to be made if nothing collapses
    return
  fillRandomCell(getZeros())
  displayGrid()

def flushUp():
  didFlush = False
  for c in range(COLUMNS):
    newCol = np.array(list(filter(lambda x: x > 0, grid[:,c])))
    if newCol.size < COLUMNS:
      didFlush = True
    newCol = np.append(newCol, np.zeros(ROWS-newCol.size))
    grid[:,c] = newCol
  return didFlush
      
def collapseDown(event):
  flushBefore = flushDown()
  for c in range(COLUMNS):
    for r in reversed(range(1, ROWS)):
      if grid[r][c] == grid[r-1][c]:
        grid[r][c] += grid[r-1][c]
        grid[r-1][c] = 0
  flushAfter = flushDown()
  if not (flushBefore or flushAfter):
    # No move to be made if nothing collapses
    return
  fillRandomCell(getZeros())
  displayGrid()

def flushDown():
  didFlush = False
  for c in range(COLUMNS):
    newCol = np.array(list(filter(lambda x: x > 0, grid[:,c])))
    if newCol.size < COLUMNS:
      didFlush = True
    newCol = np.append(np.zeros(ROWS-newCol.size), newCol)
    grid[:,c] = newCol
  return didFlush
      
def collapseLeft(event):
  flushBefore = flushLeft()
  for r in range(ROWS):
    for c in range(COLUMNS-1):
      if grid[r][c] == grid[r][c+1]:
        grid[r][c] += grid[r][c+1]
        grid[r][c+1] = 0
  flushAfter = flushLeft()
  if not (flushBefore or flushAfter):
    # No move to be made if nothing collapses
    return
  fillRandomCell(getZeros())
  displayGrid()

def flushLeft():
  didFlush = False
  for r in range(ROWS):
    newRow = np.array(list(filter(lambda x: x > 0, grid[r,:])))
    if newRow.size < ROWS:
      didFlush = True
    newRow = np.append(newRow, np.zeros(COLUMNS-newRow.size))
    grid[r,:] = newRow
  return didFlush
      
def collapseRight(event):
  flushBefore = flushRight()
  for r in range(ROWS):
    for c in reversed(range(1, COLUMNS)):
      if grid[r][c] == grid[r][c-1]:
        grid[r][c] += grid[r][c-1]
        grid[r][c-1] = 0
  flushAfter = flushRight()
  if not (flushBefore or flushAfter):
    # No move to be made if nothing collapses
    return
  fillRandomCell(getZeros())
  displayGrid()

def flushRight():
  didFlush = False
  for r in range(ROWS):
    newRow = np.array(list(filter(lambda x: x > 0, grid[r,:])))
    if newRow.size < ROWS:
      didFlush = True
    newRow = np.append(np.zeros(COLUMNS-newRow.size), newRow)
    grid[r,:] = newRow
  return didFlush
      
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
