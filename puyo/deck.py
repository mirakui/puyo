import random

class Deck():
    def __init__(self, size=128, colors=4):
        self.colors = colors
        self.size = size
        self.cards = []
        self.position = 0

    def hand(self, n=6):
        while len(self.cards) <= self.position + n:
            self._expand()
        return self.cards[self.position:(self.position+n)]

    def draw(self):
        result = self.hand(2)
        self.position += 2
        return result

    def _expand(self):
        cards = []
        for c in range(self.colors):
            cards.extend([c + 1 for i in range(int(self.size/self.colors))])

        random.shuffle(cards)
        if len(self.cards) == 0:
            while len(set(cards[0:4])) == self.colors:
                random.shuffle(cards)

        self.cards.extend(cards)

if __name__ == '__main__':
    d = Deck(size=16)
    print("end")
