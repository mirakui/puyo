from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle, Ellipse
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.core.window import Window
from board import Board

class PuyoGame(Widget):
    def __init__(self, **kwargs):
        super(PuyoGame, self).__init__(**kwargs)
        self.keyboard = Window.request_keyboard(self.keyboard_closed, self, 'text')
        self.keyboard.bind(on_key_down=self.on_key_down)

        self.board = Board()
        self.board.parse_cells("""
004000
300000
444110
312440
331221
112441
        """)

        self._running_gravitize_and_erase = False

    def update(self):
        self.render_board()

    def render_board(self):
        with self.canvas:
            for x in range(self.board.horizontal_cells):
                for y in range(self.board.vertical_cells):
                    cell = self.board.cell(x, y)
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
                        # continue

                    Ellipse(pos=(x*60, y*50), size=(60, 40))

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
        elif keycode[1] == 'down':
            self._gravitize()

        # Return True to accept the key. Otherwise, it will be used by
        # the system.
        return True

    def _gravitize(self, dt=0.0):
        if self.board.gravitize():
            self.update()
            Clock.schedule_once(self._erase, 0.5)

    def _erase(self, dt=0.0):
        if self.board.erase():
            self.update()
            Clock.schedule_once(self._gravitize, 0.5)

class PuyoApp(App):
    def build(self):
        game = PuyoGame()
        game.update()
        return game

if __name__ == '__main__':
    PuyoApp().run()
