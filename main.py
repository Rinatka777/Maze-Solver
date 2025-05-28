from graphics import Window, Line, Point, Cell

def main():
    win = Window(800, 600)
# Cell 1: all walls (default)
    cell1 = Cell(win)
    cell2 = Cell(win)
    cell3 = Cell(win)

    cell1.draw(50, 50, 100, 100)
    cell2.draw(100, 50, 150, 100)
    cell3.draw(150, 50, 200, 100)

    cell1.draw_move(cell2)          # red move forward
    cell2.draw_move(cell3)          # red move forward
    cell3.draw_move(cell2, undo=False)  # gray backtrack
    cell2.draw_move(cell1, undo=True)  # gray backtrack

    win.wait_for_close()


if __name__ == "__main__":
    main()