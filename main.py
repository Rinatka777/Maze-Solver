from graphics import Window, Line, Point


def main():
    win = Window(800, 600)
    l = Line(Point(50, 50), Point(400, 400))
    win.draw_line(l, "black")

    l = Line(Point(30, 400), Point(300, 300))
    win.draw_line(l, "red")
    
    win.wait_for_close()

if __name__ == "__main__":
    main()