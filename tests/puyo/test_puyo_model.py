from unittest import TestCase
from puyo.puyo_model import PuyoModel

class TestPuyoModel(TestCase):
    def test_foo(self):
        self.assertEqual('a', 'b')

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
