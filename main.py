from graphics import Window, Line, Point, Cell, Maze

def main():
    print("Maze initialized.")

    win = Window(800, 600)
# Cell 1: all walls (default)
    maze = Maze(
        x1=50,
        y1=50,
        num_rows=10,
        num_cols=15,
        cell_size_x=40,
        cell_size_y=40,
        win=win,
    )
    maze.solve()
    win.wait_for_close()
    

if __name__ == "__main__":
    main()