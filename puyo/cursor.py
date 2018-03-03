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
            self.horizontal_cells * 4 - 2
        ]

    def reset_position(self):
        self.set_position(int((self.horizontal_cells - 1)/ 2))

    def set_position(self, position):
        self.position = position

    def move(self, direction):
        for i in range(len(self.ranges) - 1):
            rng = range(self.ranges[i], self.ranges[i+1])
            if self.position in rng:
                return self._move(direction, rng)

        return self.position

    def _move(self, direction, rng):
        if direction == Direction.Left:
            self.position = max(rng.start, self.position - 1)
        elif direction == Direction.Right:
            self.position = min(self.position + 1, rng.stop - 1)
        return self.position

    def turn(self, direction):
        if direction == Direction.Left:
            self.set_position(self._turn_left(self.position))
        elif direction == Direction.Right:
            self.set_position(self._turn_right(self.position))

    def _turn_left(self, i):
        if i in range(self.ranges[0], self.ranges[1]):
            return max(i + (self.horizontal_cells - 1), self.horizontal_cells)
        elif i in range(self.ranges[1], self.ranges[2]):
            return i + self.horizontal_cells
        elif i in range(self.ranges[2], self.ranges[3]):
            return min(i + self.horizontal_cells, self.ranges[4] - 1)
        elif i in range(self.ranges[3], self.ranges[4]):
            return (i + 1) % self.horizontal_cells

    def _turn_right(self, i):
        if i in range(self.ranges[0], self.ranges[1]):
            return min(i + self.ranges[3], self.ranges[4] - 1)
        elif i in range(self.ranges[1], self.ranges[2]):
            return i - self.horizontal_cells + 1
        elif i in range(self.ranges[2], self.ranges[3]):
            return max(i - self.horizontal_cells, self.horizontal_cells)
        elif i in range(self.ranges[3], self.ranges[4]):
            return i - self.horizontal_cells

    def get_axis(self, position=None):
        if isinstance(position, int):
            i = position
        else:
            i = self.position

        if i in range(self.ranges[0], self.ranges[1]):
            return [[i, 1], [i, 2]]
        elif i in range(self.ranges[1], self.ranges[2]):
            j = i % self.horizontal_cells
            return [[j + 1, 1], [j, 1]]
        elif i in range(self.ranges[2], self.ranges[3]):
            j = (i + 1) % self.horizontal_cells
            return [[j, 1], [j, 0]]
        elif i in range(self.ranges[3], self.ranges[4]):
            j = (i + 1) % self.horizontal_cells
            return [[j, 1], [j + 1, 1]]

class Direction(Enum):
    Left = "left"
    Right = "right"

if __name__ == '__main__':
    c = Cursor()
    for i in range(22):
        print(i, c.get_axis(position=i))
