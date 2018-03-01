from enum import Enum

class Cursor():

    def __init__(self, horizontal_cells=6):
        self.horizontal_cells = horizontal_cells
        self.position = None
        self.reset_position()
        self.ranges = [
            0,
            self.horizontal_cells,
            self.horizontal_cells * 2 - 1,
            self.horizontal_cells * 3 - 1,
            self.horizontal_cells * 4 - 3
        ]

    def reset_position(self):
        self.set_position(int((self.horizontal_cells - 1)/ 2))

    def set_position(self, position):
        self.position = position

    def move(self, direction):
        for i in range(len(self.ranges) - 1):
            rng = range(self.ranges[i], self.ranges[i+1])
            if self.position in rng:
                self._move(direction, rng)
                break

        return self.position

    def _move(self, direction, rng):
        if direction == Direction.Left:
            self.position = max(rng.start, self.position - 1)
        elif direction == Direction.Right:
            self.position = min(self.position + 1, rng.stop - 1)

class Direction(Enum):
    Left = "left"
    Right = "right"
