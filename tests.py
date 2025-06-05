import unittest
# assuming your `Maze` class is in a file called `maze.py`
from graphics import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._Maze__cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._Maze__cells[0]),
            num_rows,
        )

    def test_break_and_exit(self):
        num_cols = 5
        num_rows = 5
        m = Maze(0, 0, num_rows, num_cols, 10, 10)

        m._Maze__break_entrance_and_exit()
        entrance = m._Maze__cells[0][0]
        self.assertFalse(entrance.has_top_wall, "Top wall of entrance should be removed")

        # Check exit
        exit_cell = m._Maze__cells[-1][-1]
        self.assertFalse(exit_cell.has_bottom_wall, "Bottom wall of exit should be removed")


if __name__ == "__main__":
    unittest.main()