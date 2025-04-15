import tkinter as tk

# Constants for the grid and eraser dimensions
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40      # Each cell is 40x40 pixels
ERASER_SIZE = 50    # Eraser is 50x50 pixels (square)

def drag_eraser(event):
    """
    Callback for dragging the eraser.
    Moves the eraser rectangle to center on the current mouse position,
    and then erases (turns white) any cell that overlaps with it.
    """
    # Calculate new coordinates for the eraser rectangle so that it centers at the mouse position
    half = ERASER_SIZE // 2
    x1, y1 = event.x - half, event.y - half
    x2, y2 = event.x + half, event.y + half

    # Update the position of the eraser rectangle
    canvas.coords(eraser, x1, y1, x2, y2)

    # Find all items that overlap the eraser rectangle's new position
    overlapping_items = canvas.find_overlapping(x1, y1, x2, y2)
    for item in overlapping_items:
        # Check if the item is one of our blue cells using its tag "cell"
        if "cell" in canvas.gettags(item):
            # Change the cell's fill color to white
            canvas.itemconfig(item, fill="white")

# Create the main window
root = tk.Tk()
root.title("Canvas Eraser")

# Create a Canvas widget
canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
canvas.pack()

# Draw a grid of blue cells on the canvas
for row in range(0, CANVAS_HEIGHT, CELL_SIZE):
    for col in range(0, CANVAS_WIDTH, CELL_SIZE):
        # Create a rectangle for each cell
        # Tag each rectangle with "cell" so that we can identify them later
        canvas.create_rectangle(col, row, col + CELL_SIZE, row + CELL_SIZE,
                                fill="blue", outline="black", tags="cell")

# Create the eraser rectangle.
# Start it in the upper-left corner.
eraser = canvas.create_rectangle(0, 0, ERASER_SIZE, ERASER_SIZE,
                                 fill="gray", outline="black", stipple="gray50")

# Bind the left mouse button drag event to the drag_eraser function
canvas.bind("<B1-Motion>", drag_eraser)

# Start the GUI event loop
root.mainloop()


