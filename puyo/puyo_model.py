from enum import Enum

class PuyoModel():
    def __init__(self, vertical_cells=13, horizontal_cells=6, colors=4, min_chain_size=4):
        self.vertical_cells = vertical_cells
        self.horizontal_cells = horizontal_cells
        self.colors = colors
        self.max_combo = 0
        self.min_chain_size = min_chain_size

        self.zerofill_cells()

    def dump(self):
        for y in reversed(range(self.vertical_cells)):
            for x in range(self.horizontal_cells):
                cell = self.cells[self.cell_index(x, y)]
                print(cell, end='')
            print('')

    def zerofill_cells(self):
        self.cells = [0 for i in range(self.vertical_cells * self.horizontal_cells)]

    def parse_cells(self, text):
        self.zerofill_cells()
        y = 0
        for line in reversed(text.split()):
            x = 0
            for c in list(line):
                self.cells[self.cell_index(x, y)] = int(c)
                x += 1
            y += 1

        return self.cells

    def erase(self):
        marks = [ErasingMark.Unmarked for i in range(len(self.cells))]

        for y in range(self.vertical_cells):
            for x in range(self.horizontal_cells):
                chain = [self.cell_index(x, y)]
                self._find_chain(x, y, marks, chain)
                if len(chain) >= self.min_chain_size:
                    for idx in chain:
                        self.cells[idx] = 0

        return self.cells

    def _find_chain(self, x, y, marks, chain, chain_color=0):
        idx = self.cell_index(x, y)

        if marks[idx] != ErasingMark.Unmarked:
            return chain

        color = self.cells[idx]
        if color == 0:
            return chain
        elif color == chain_color:
            chain.append(idx)
        elif chain_color != 0 and color != chain_color:
            return chain

        marks[idx] = ErasingMark.Checking

        if 0 < x:
            self._find_chain(x-1, y, marks, chain=chain, chain_color=color)

        if x + 1 < self.horizontal_cells:
            self._find_chain(x+1, y, marks, chain=chain, chain_color=color)

        if 0 < y:
            self._find_chain(x, y-1, marks, chain=chain, chain_color=color)

        if y + 1 < self.vertical_cells:
            self._find_chain(x, y+1, marks, chain=chain, chain_color=color)

        marks[idx] = ErasingMark.Marked

        return chain

    def cell_index(self, x, y):
        return x + y * self.horizontal_cells


class ErasingMark(Enum):
    Unmarked = 'not marked yet'
    Checking = 'under checking'
    Marked = 'marked'

if __name__ == '__main__':
    model = PuyoModel()
    model.parse_cells("""
123441
233141
334341
443442
    """)
    model.dump()
    print("\n")
    model.erase()
    model.dump()
