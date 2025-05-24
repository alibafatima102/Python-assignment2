import tkinter as tk

# Constants
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20

class EraserApp:
    def __init__(self, root):
        self.canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
        self.canvas.pack()
        self.cells = []
        self.create_grid()
        self.eraser = None
        self.canvas.bind("<Button-1>", self.create_eraser)
        self.canvas.bind("<B1-Motion>", self.move_eraser)

    def create_grid(self):
        for row in range(0, CANVAS_HEIGHT, CELL_SIZE):
            for col in range(0, CANVAS_WIDTH, CELL_SIZE):
                cell = self.canvas.create_rectangle(
                    col, row, col + CELL_SIZE, row + CELL_SIZE,
                    fill="blue", outline="black"
                )
                self.cells.append(cell)

    def create_eraser(self, event):
        if not self.eraser:
            self.eraser = self.canvas.create_rectangle(
                event.x, event.y, event.x + ERASER_SIZE, event.y + ERASER_SIZE,
                fill="pink", outline=""
            )

    def move_eraser(self, event):
        if self.eraser:
            self.canvas.coords(
                self.eraser,
                event.x, event.y,
                event.x + ERASER_SIZE, event.y + ERASER_SIZE
            )
            self.erase(event.x, event.y)

    def erase(self, x, y):
        # Get eraser bounding box
        ex1, ey1 = x, y
        ex2, ey2 = x + ERASER_SIZE, y + ERASER_SIZE
        # Check each cell for overlap
        for cell in self.cells:
            cx1, cy1, cx2, cy2 = self.canvas.coords(cell)
            if not (ex2 < cx1 or ex1 > cx2 or ey2 < cy1 or ey1 > cy2):
                self.canvas.itemconfig(cell, fill="white")

def main():
    root = tk.Tk()
    root.title("Eraser Tool Example")
    app = EraserApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
