import tkinter as tk

from grid import Grid

ROWS, COLUMNS = 4, 4
TILE_COLORS: dict[int, str] = {
    0:    '#cdc1b4',
    2:    '#eee4da',
    4:    '#ede0c8',
    8:    '#f2b179',
    16:   '#f59563',
    32:   '#f67c5f',
    64:   '#f65e3b',
    128:  '#edcf72',
    256:  '#edcc61',
    512:  '#edc850',
    1024: '#edc53f',
    2048: '#edc22e',
}

DARK_TEXT = '#776e65'
LIGHT_TEXT = '#f9f6f2'

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
        root.configure(bg='#bbada0')

        frame = tk.Frame(root, bg='#bbada0')
        for r in range(ROWS):
            display_row: list[tk.Label] = []
            for c in range(COLUMNS):
                label = tk.Label(
                    frame, bg='#cdc1b4', fg=DARK_TEXT,
                    width=6, height=3,
                    font=('Helvetica', 36, 'bold'),
                )
                label.grid(row=r, column=c, padx=6, pady=6)
                display_row.append(label)
            self.display.append(display_row)
        frame.pack(padx=20, pady=20)

        tk.Button(
            root, text='Restart', command=self.restart,
            highlightbackground='#bbada0', fg=DARK_TEXT,
            font=('Helvetica', 14, 'bold'),
            padx=20, pady=6,
        ).pack(pady=(0, 20))

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
                display_color = TILE_COLORS.get(value, '#3c3a32')
                text_color = DARK_TEXT if value in (0, 2, 4) else LIGHT_TEXT
                self.display[r][c].config(
                    text=display_text, bg=display_color, fg=text_color,
                )


def main() -> None:
    root = tk.Tk()
    Game(root)
    root.mainloop()


if __name__ == '__main__':
    main()
