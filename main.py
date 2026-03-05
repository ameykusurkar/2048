import tkinter as tk

from grid import Grid

ROWS, COLUMNS = 4, 4
TILE_COLORS: dict[int, str] = {
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

DIRECTION_KEYS: dict[str, str] = {
    'Up': 'up',
    'Down': 'down',
    'Left': 'left',
    'Right': 'right',
}


class Game:
    def __init__(self, root: tk.Tk) -> None:
        self.grid = Grid(rows=ROWS, columns=COLUMNS)
        self.display: list[list[tk.Label]] = []

        root.wm_title('2048')

        frame = tk.Frame(root, height=500, width=500, bg='#606060')
        for r in range(ROWS):
            display_row: list[tk.Label] = []
            for c in range(COLUMNS):
                label = tk.Label(
                    frame, bg='#E74C3C', fg='white',
                    borderwidth=10, width=4, height=2,
                    font=('Arial', 28),
                )
                label.grid(row=r, column=c, padx=3, pady=3)
                display_row.append(label)
            self.display.append(display_row)
        frame.pack()

        tk.Button(root, text='Restart', command=self.restart).pack()

        for key in DIRECTION_KEYS:
            root.bind(f'<{key}>', self._on_key)

        self.restart()

    def restart(self) -> None:
        self.grid.restart()
        self._update_display()

    def _on_key(self, event: tk.Event) -> None:  # type: ignore[type-arg]
        direction = DIRECTION_KEYS.get(event.keysym)
        if direction is None:
            return
        move = getattr(self.grid, direction)
        if move():
            self._update_display()

    def _update_display(self) -> None:
        for r in range(ROWS):
            for c in range(COLUMNS):
                value = self.grid.value_at(r, c)
                display_text = '' if value == 0 else str(value)
                display_color = TILE_COLORS.get(value, 'black')
                self.display[r][c].config(text=display_text, bg=display_color)


def main() -> None:
    root = tk.Tk()
    Game(root)
    root.mainloop()


if __name__ == '__main__':
    main()
