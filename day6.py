"""--- Day 6: Chronal Coordinates ---
The device on your wrist beeps several times, and once again you feel 
like you're falling.

"Situation critical," the device announces. "Destination indeterminate. 
Chronal interference detected. Please specify new target coordinates."

The device then produces a list of coordinates (your puzzle input). Are 
they places it thinks are safe or dangerous? It recommends you check 
manual page 729. The Elves did not give you a manual.

If they're dangerous, maybe you can minimize the danger by finding the 
coordinate that gives the largest distance from the other points.

Using only the Manhattan distance, determine the area around each 
coordinate by counting the number of integer X,Y locations that are 
closest to that coordinate (and aren't tied in distance to any other 
coordinate).

Your goal is to find the size of the largest area that isn't infinite. 
For example, consider the following list of coordinates:

1, 1
1, 6
8, 3
3, 4
5, 5
8, 9
If we name these coordinates A through F, we can draw them on a 
grid, putting 0,0 at the top left:

..........
.A........
..........
........C.
...D......
.....E....
.B........
..........
..........
........F.
This view is partial - the actual grid extends infinitely in all 
directions. Using the Manhattan distance, each location's closest 
coordinate can be determined, shown here in lowercase:

aaaaa.cccc
aAaaa.cccc
aaaddecccc
aadddeccCc
..dDdeeccc
bb.deEeecc
bBb.eeee..
bbb.eeefff
bbb.eeffff
bbb.ffffFf
Locations shown as . are equally far from two or more coordinates, 
and so they don't count as being closest to any.

In this example, the areas of coordinates A, B, C, and F are infinite - 
while not shown here, their areas extend forever outside the visible grid. 
However, the areas of coordinates D and E are finite: D is closest to 9 
locations, and E is closest to 17 (both including the coordinate's 
location itself). Therefore, in this example, the size of the largest 
area is 17.
What is the size of the largest area that isn't infinite?
"""
import utils


class Grid:
    """Matrix class to abstract the rows & columns"""

    def __init__(self, size, points):
        self._matrix = []
        self._size = size
        # pylint: disable=W0612
        for i in range(0, size):
            self._matrix.append([None]*size)
        self._points = points

    def size(self):
        """Return the size of the matrix"""
        assert self._matrix is not None and len(
            self._matrix) == len(self._matrix[0])
        return len(self._matrix)

    def mark(self, row, column, marker):
        """Mark row, column  in matrix with marker"""
        self._matrix[column][row] = marker

    def get(self, r, c):
        return self._matrix[c][r]

    def limits(self):
        """Determine the search boundaries, i.e. retrieve the
           minimum and maximum rows and columns from the set of points.
           All possibly qualifying points lie within these boundaries.
        """
        if self._points is not None and len(self._points) > 0:
            self._minrow = sorted(
                self._points, key=lambda p: p[1], reverse=False)[0][1]
            self._maxrow = sorted(
                self._points, key=lambda p: p[1], reverse=True)[0][1]
            self._mincol = sorted(
                self._points, key=lambda p: p[0], reverse=False)[0][0]
            self._maxcol = sorted(
                self._points, key=lambda p: p[0], reverse=True)[0][0]
        return (self._minrow, self._maxrow, self._mincol, self._maxcol)

    def paint(self):
        """Determine the grid's closest neighbour; if it is a single
        point, the value will the the points sequence number.
        Otherwise, it will be a '.'.
        """
        for row in range(self._size):
            for col in range(self._size):
                distances = []
                for i in range(len(self._points)):
                    distances.append((i, manhattan_distance(
                        col, row, self._points[i][0], self._points[i][1])))
                # all distances calculated.
                all_dist = sorted(distances, key=lambda t: t[1])
                if all_dist[0][0] < all_dist[1][0]:
                    self.mark(row, col, all_dist[0][0])
                else:
                    self.mark(row, col, '.')


def line_to_point(line):
    elements = line.split(',')
    return (int(elements[0]), int(elements[1]))


def read_points(fname):
    return utils.read_file(filename=fname, convert=line_to_point)


def manhattan_distance(col1, row1, col2, row2):
    return abs(row1-row2) + abs(col1-col2)
