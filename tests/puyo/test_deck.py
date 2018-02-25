from unittest import TestCase
from puyo.deck import Deck

class TestDeck(TestCase):
    def test_hand(self):
        deck = Deck()
        hand = deck.hand()
        self.assertEqual(len(hand), 6)

    def test_hand2(self):
        for i in range(100):
            deck = Deck()
            hand = deck.hand(4)
            self.assertIn(len(set(hand)), {1, 2, 3})

    def test_hand3(self):
        deck = Deck(size=128)
        hand128 = deck.hand(128)
        hand256 = deck.hand(256)
        self.assertEqual(sum(hand128), (1+2+3+4)*32)
        self.assertEqual(sum(hand256), (1+2+3+4)*64)
        self.assertListEqual(hand128, hand256[0:128])
        self.assertSetEqual(set(hand256), {1, 2, 3, 4})
