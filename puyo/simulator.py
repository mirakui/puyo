from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock

class PuyoGame(Widget):
    board = ObjectProperty(None)


class PuyoApp(App):
    def build(self):
        game = PuyoGame()
        return game

if __name__ == '__main__':
    PuyoApp().run()
