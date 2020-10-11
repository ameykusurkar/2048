import tkinter as tk

from grid import Grid

ROWS, COLUMNS = 4, 4
TILE_COLORS = {
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

grid = Grid(rows=ROWS, columns=COLUMNS)
display = []

def restart():
    grid.restart()
    display_grid()

def display_grid():
    for r in range(ROWS):
        for c in range(COLUMNS):
            value = grid.value_at(r, c)
            display_text = '' if value == 0 else str(value)
            display_color = TILE_COLORS.get(value, 'black')
            display[r][c].config(text=display_text, bg=display_color)

def key_up(event):
    grid_did_change = grid.up()
    if grid_did_change:
        display_grid()

def key_down(event):
    grid_did_change = grid.down()
    if grid_did_change:
        display_grid()

def key_left(event):
    grid_did_change = grid.left()
    if grid_did_change:
        display_grid()

def key_right(event):
    grid_did_change = grid.right()
    if grid_did_change:
        display_grid()

##### GUI and Game setup #####

root = tk.Tk()
root.wm_title('2048')

F = tk.Frame(root, height=500, width=500, bg='#606060')
B = tk.Button(root, text='Restart', command=restart)

for r in range(ROWS):
    display_row = []
    for c in range(COLUMNS):
        new_label = tk.Label(F, bg='#E74C3C', fg='white',
                             borderwidth=10,
                             width=4, height=2,
                             font=('Arial', 28))
        new_label.grid(row=r,column=c, padx=3, pady=3)
        display_row.append(new_label)
    display.append(display_row)

F.pack()
B.pack()

root.bind('<Up>', key_up)
root.bind('<Down>', key_down)
root.bind('<Left>', key_left)
root.bind('<Right>', key_right)

grid.restart()
display_grid()
root.mainloop()
