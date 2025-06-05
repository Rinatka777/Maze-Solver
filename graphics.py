from tkinter import Tk, BOTH, Canvas
import time


class Window:
    def __init__(self, width, height): #so here i basically create a "canvas" on which the action will happen - empty list sort of
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False

    def redraw(self): # redraw all the graphics in the window
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("window closed...")


    def draw_line(self, line, fill_color):
        line.draw(self.__canvas, fill_color)
    
    def close(self): 
        self.__running = False


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, p1, p2):
      self.p1 = p1
      self.p2 = p2
    
    def draw(self, canvas, fill_color = "black"):
        canvas.create_line(
            self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2
        )

class Cell:
    def __init__(self, win = None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1
        self.__win = win

    def draw(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2

        if self.__win is None:
            return
        
        bg_color = "white"

# Top wall (draw either way!)
        if self.has_top_wall:
            color = "black"
        else:
            color = bg_color

        top = Line(Point(x1, y1), Point(x2, y1))
        self.__win.draw_line(top, color)


        if self.has_right_wall:
            right = Line(Point(x2, y1), Point(x2, y2))
            self.__win.draw_line(right, "black")

        if self.has_bottom_wall:
            color = "black"
        else:
            color = bg_color

        bottom = Line(Point(x1, y2), Point(x2, y2))
        self.__win.draw_line(bottom, color)


        if self.has_left_wall:
            left = Line(Point(x1, y1), Point(x1, y2))
            self.__win.draw_line(left, "black")

    def draw_move(self, to_cell, undo=False):
        if self.__win is None:
            return
        x1 = (self.__x1 + self.__x2) // 2
        y1 = (self.__y1 + self.__y2) // 2
        x2 = (to_cell.__x1 + to_cell.__x2) // 2
        y2 = (to_cell.__y1 + to_cell.__y2) // 2

        color = "gray" if undo else "red"
        move_line = Line(Point(x1, y1), Point(x2, y2))
        self.__win.draw_line(move_line, color)

class Maze:
    def __init__(self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win = None):

        self.__x1 = x1
        self.__y1 = y1
        self.__rows = num_rows
        self.__cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win

        self.__cells = []  # 2D list: columns of rows
        self.__create_cells()
        self.__break_entrance_and_exit()


    def __create_cells(self):
        for i in range(self.__cols):
            column = []
            for j in range(self.__rows):
                cell = Cell(self.__win)
                column.append(cell)
            self.__cells.append(column)
        
        for i in range(self.__cols):
            for j in range(self.__rows):
                self.__draw_cell(i, j)
    
    def __draw_cell(self, i, j):
        x1 = self.__x1 + i * self.__cell_size_x
        y1 = self.__y1 + j * self.__cell_size_y
        x2 = x1 + self.__cell_size_x
        y2 = y1 + self.__cell_size_y
        
        self.__cells[i][j].draw(x1, y1, x2, y2)
        self.animate()

    def animate(self):
        if self.__win is None:
            return
        self.__win.redraw()
        time.sleep(0.05)
    
    def __break_entrance_and_exit(self):
        self.__cells[0][0].has_top_wall = False
        self. __draw_cell(0, 0)

        last_col = self.__cols - 1
        last_row = self.__rows - 1

        self.__cells[last_col][last_row].has_bottom_wall = False
        self. __draw_cell(last_col, last_row)



    



         
                       





