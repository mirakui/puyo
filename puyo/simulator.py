from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle, Ellipse
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock

class PuyoApp(App):
    def build(self):
        root = Widget()

        with root.canvas:
            for x in range(6):
                for y in range(10):
                    Color(1, 0, 0, 1, mode='rgba')
                    Ellipse(pos=(x*60, y*50), size=(60, 40))

        return root

if __name__ == '__main__':
    PuyoApp().run()
