class PuyoModel():
    def __init__(self, vertical_cells=13, horizontal_cells=6, colors=4):
        self.vertical_cells = vertical_cells
        self.horizontal_cells = horizontal_cells
        self.colors = colors
        self.max_combo = 0

        self.zerofill_cells()

    def dump(self):
        for y in reversed(range(self.vertical_cells)):
            for x in range(self.horizontal_cells):
                cell = self.cells[x + y * self.horizontal_cells]
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
                self.cells[x + y * self.horizontal_cells] = int(c)
                x += 1
            y += 1

if __name__ == '__main__':
    model = PuyoModel()
    model.parse_cells("""
21
111
23244
22322
33244
    """)
    model.dump()
