from unittest import TestCase
from puyo.puyo_model import PuyoModel

class TestPuyoModel(TestCase):

    def test_parse_cells(self):
        m = PuyoModel()
        text = """
21
111
23244
22322
33244
        """
        m.parse_cells(text)

        self.assertEqual(
            m.cells,
            [
                3, 3, 2, 4, 4, 0,
                2, 2, 3, 2, 2, 0,
                2, 3, 2, 4, 4, 0,
                1, 1, 1, 0, 0, 0,
                2, 1, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0
            ]
        )

    def test_erase(self):
        m = PuyoModel()
        m.parse_cells("""
123441
233141
334341
443442
        """)
        m.erase()

        expected = PuyoModel()
        expected.parse_cells("""
120001
200101
004301
443002
        """)
        self.assertEqual(m.cells, expected.cells)

    def test_gravitize(self):
        m = PuyoModel()
        m.parse_cells("""
443440
010001
112002
400020
300011
        """)
        m.gravitize()

        expected = PuyoModel()
        expected.parse_cells("""
400000
140041
413022
312411
        """)
        self.assertEqual(m.cells, expected.cells)

    def test_gravitize_and_erase(self):
        m = PuyoModel()
        m.parse_cells("""
004000
300000
444010
312441
331221
112441
        """)
        m.gravitize_and_erase()

        expected = PuyoModel()
        expected.parse_cells("""
000000
000000
000000
000000
000000
000000
        """)
        self.assertEqual(m.cells, expected.cells)
