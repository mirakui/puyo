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
