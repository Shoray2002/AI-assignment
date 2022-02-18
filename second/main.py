from kivy.uix.label import Label
from kivy.app import App
from kivy.uix.behaviors import DragBehavior
from kivy.lang import Builder

# You could also put the following in your kv file...
# Builder.load_file('main.kv')

class DragLabel(DragBehavior, Label):
    pass


class TestApp(App):
    def build(self):
        return Builder.load_file('main.kv')

TestApp().run()