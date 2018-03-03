from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle, Ellipse
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.core.window import Window
from board import Board
from deck import Deck
from cursor import Cursor, Direction

class PuyoGame(Widget):
    def __init__(self, **kwargs):
        super(PuyoGame, self).__init__(**kwargs)
        self.keyboard = Window.request_keyboard(self.keyboard_closed, self, 'text')
        self.keyboard.bind(on_key_down=self.on_key_down)

        self.board = Board()
        self.board.parse_cells("""
000000
300000
444110
312440
331221
112441
        """)
        self.deck = Deck()
        self.cursor = Cursor()

        self.erasing = False

    def update(self):
        self.render_board()
        self.render_cursor()
        self.render_hand()

    def render_board(self):
        for x in range(self.board.horizontal_cells):
            for y in range(self.board.vertical_cells):
                cell = self.board.cell(x, y)
                self.render_puyo_in_grid(pos=(x, y), cell=cell)

    def render_puyo(self, pos, cell):
        with self.canvas:
            if cell == 1:
                Color(1, 0, 0, 1, mode='rgba')
            elif cell == 2:
                Color(0, 1, 0, 1, mode='rgba')
            elif cell == 3:
                Color(0, 0, 1, 1, mode='rgba')
            elif cell == 4:
                Color(1, 1, 0, 1, mode='rgba')
            else:
                Color(0, 0, 0, 1, mode='rgba')

            Ellipse(pos=pos, size=(60, 40))

    def clear_hand(self):
        with self.canvas:
            Color(0, 0, 0, 1, mode='rgba')
            Rectangle(
                pos=(0, self.board.vertical_cells * 50),
                size=(self.board.horizontal_cells * 60, 3 * 50)
            )

    def render_cursor(self):
        hand = self.deck.hand()
        axis = self.cursor.axis()

        self.clear_hand()
        self.render_puyo_in_grid(
            pos=(axis[0][0], axis[0][1] + self.board.vertical_cells),
            cell=hand[0]
        )
        self.render_puyo_in_grid(
            pos=(axis[1][0], axis[1][1] + self.board.vertical_cells),
            cell=hand[1]
        )

    def render_puyo_in_grid(self, pos, cell):
        self.render_puyo(pos=(pos[0]*60, pos[1]*50), cell=cell)

    def render_hand(self):
        hand = self.deck.hand()

        self.render_puyo_in_grid(
            pos=(self.board.horizontal_cells + 2, self.board.vertical_cells - 2),
            cell=hand[2]
        )
        self.render_puyo_in_grid(
            pos=(self.board.horizontal_cells + 2, self.board.vertical_cells - 1),
            cell=hand[3]
        )
        self.render_puyo_in_grid(
            pos=(self.board.horizontal_cells + 3, self.board.vertical_cells - 2),
            cell=hand[4]
        )
        self.render_puyo_in_grid(
            pos=(self.board.horizontal_cells + 3, self.board.vertical_cells - 1),
            cell=hand[5]
        )

    def keyboard_closed(self):
        print('My keyboard have been closed!')
        self.keyboard.unbind(on_key_down=self.on_key_down)
        self.keyboard = None

    def on_key_down(self, keyboard, keycode, text, modifiers):
        print('The key', keycode, 'have been pressed')
        print(' - text is %r' % text)
        print(' - modifiers are %r' % modifiers)

        # Keycode is composed of an integer + a string
        # If we hit escape, release the keyboard
        if keycode[1] == 'escape':
            keyboard.release()
        elif not self.erasing and keycode[1] == 'down':
            self.draw_hand()
            self.gravitize()
            self.render_board()
            self.render_cursor()
        elif keycode[1] == 'left':
            self.cursor.move(Direction.Left)
            self.render_cursor()
        elif keycode[1] == 'right':
            self.cursor.move(Direction.Right)
            self.render_cursor()
        elif keycode[1] == 'z':
            self.cursor.turn(Direction.Left)
            self.render_cursor()
        elif keycode[1] == 'x':
            self.cursor.turn(Direction.Right)
            self.render_cursor()

        # Return True to accept the key. Otherwise, it will be used by
        # the system.
        return True

    def draw_hand(self):
        hand = self.deck.draw()
        axis = self.cursor.axis()
        self.cursor.reset_position()

        self.board.set_cell(axis[0][0], axis[0][1] + self.board.vertical_cells - 3, hand[0])
        self.board.set_cell(axis[1][0], axis[1][1] + self.board.vertical_cells - 3, hand[1])

        self.render_hand()

    def gravitize(self, dt=0.0):
        if self.board.gravitize():
            self.update()
            self.erasing = True
            Clock.schedule_once(self.erase, 0.5)
        else:
            self.erasing = False

    def erase(self, dt=0.0):
        if self.board.erase():
            self.update()
            Clock.schedule_once(self.gravitize, 0.5)
        else:
            self.erasing = False

class PuyoApp(App):
    def build(self):
        game = PuyoGame()
        game.update()
        return game

if __name__ == '__main__':
    PuyoApp().run()
