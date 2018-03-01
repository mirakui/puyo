from unittest import TestCase
from puyo.cursor import Cursor, Direction

class TestCursor(TestCase):
    def test_move_left(self):
        cursor = Cursor()
        table = [
            # 0-5
            0, 0, 1, 2, 3, 4,
            # 6-10
            6, 6, 7, 8, 9,
            # 11-16
            11, 11, 12, 13, 14, 15,
            # 17-21
            17, 17, 18, 19, 20
        ]

        for i in range(len(table)):
            cursor.set_position(i)
            cursor.move(Direction.Left)
            self.assertEqual(cursor.position, table[i])

    def test_move_right(self):
        cursor = Cursor()
        table = [
            # 0-5
            1, 2, 3, 4, 5, 5,
            # 6-10
            7, 8, 9, 10, 10,
            # 11-16
            12, 13, 14, 15, 16, 16,
            # 17-20
            18, 19, 20, 21, 21
        ]

        for i in range(len(table)):
            cursor.set_position(i)
            cursor.move(Direction.Right)
            self.assertEqual(cursor.position, table[i])

    def test_turn_left(self):
        cursor = Cursor()
        table = [
            # 0-5
            6, 6, 7, 8, 9, 10,
            # 6-10
            12, 13, 14, 15, 16,
            # 11-16
            17, 18, 19, 20, 21, 21,
            # 17-20
            0, 1, 2, 3, 4
        ]

        for i in range(len(table)):
            cursor.set_position(i)
            cursor.turn(Direction.Left)
            self.assertEqual(cursor.position, table[i])

    def test_turn_right(self):
        cursor = Cursor()
        table = [
            # 0-5
            17, 18, 19, 20, 21, 21,
            # 6-10
            1, 2, 3, 4, 5,
            # 11-16
            6, 6, 7, 8, 9, 10,
            # 17-20
            11, 12, 13, 14, 15
        ]

        for i in range(len(table)):
            cursor.set_position(i)
            cursor.turn(Direction.Right)
            self.assertEqual(cursor.position, table[i])

    def test_get_axis(self):
        cursor = Cursor()
        table = [
            # 0-5
            [0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5],
            # 6-10
            [1, 0], [2, 1], [3, 2], [4, 3], [5, 4],
            # 11-16
            [0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5],
            # 17-20
            [0, 1], [1, 2], [2, 3], [3, 4], [4, 5]
        ]

        for i in range(len(table)):
            cursor.set_position(i)
            self.assertEqual(cursor.get_axis(), table[i])
