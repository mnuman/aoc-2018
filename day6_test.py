import day6
import random


def test_matrix():
    size = 10
    m = day6.Grid(size, [])
    assert m.size() == size


def test_mark_matrix():
    size = 10
    m = day6.Grid(size, [])
    m.mark(0, 0, 'X')
    assert m.get(0, 0) == 'X'


def test_mark_matrix_xy():
    size = 10
    row = random.randint(0, size - 1)
    col = random.randint(0, size - 1)
    m = day6.Grid(size, [])
    m.mark(row, col, 'AAP')
    assert m.get(row, col) == 'AAP'


def test_read():
    points = day6.read_points('data/day6-test.txt')
    assert len(points) == 6
    assert points[0] == (1, 1)
    assert points[5] == (8, 9)


def test_points():
    # point = col,row
    points = [(1, 1),
              (1, 6),
              (8, 3),
              (3, 4),
              (5, 5),
              (8, 9)]

    m = day6.Grid(10, points)
    limits = m.limits()
    # minrow, maxrow, mincol, maxcol
    assert limits == (1, 9, 1, 8)


def test_manhattan_distance_p1_p2():
    # all variations must yield the same result!
    assert day6.manhattan_distance(10, 0, 0, 0) == 10
    assert day6.manhattan_distance(0, 10, 0, 0) == 10
    assert day6.manhattan_distance(0, 0, 10, 0) == 10
    assert day6.manhattan_distance(0, 0, 0, 10) == 10


def test_manhattan_distance_permuations():
    assert day6.manhattan_distance(1, 2, 8, 9) == 14
    assert day6.manhattan_distance(
        1, 2, 8, 9) == day6.manhattan_distance(8, 9, 1, 2)


def test_paint():
    # point = col,row
    points = [(1, 1),
              (1, 6),
              (8, 3),
              (3, 4),
              (5, 5),
              (8, 9)]

    m = day6.Grid(10, points)
    m.paint()
    print(m)
    assert m._matrix[0] == [0,0,0,0,0,'.',1,1,1,1]
