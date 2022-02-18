import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.animation import Animation

Builder.load_file('main.kv')


class MainLayout(Widget):
    def __init__(self, **kwargs):
        super(MainLayout, self).__init__(**kwargs)
        self.right_flag = False
        self.left_flag = False

    def right_toggle(self, toggle):
        if toggle.state == 'down':
            # print('right toggle is down')
            self.ids['"right"'].size_hint = (0.5, 0.5)
            self.right_flag = True
        else:
            self.ids['"right"'].size_hint = (0, 0)
            self.right_flag = False

    def left_toggle(self, toggle):
        if toggle.state == 'down':
            self.ids['"left"'].size_hint = (0.5, 0.5)
            self.left_flag = True
        else:
            self.ids['"left"'].size_hint = (0, 0)
            self.left_flag = False

    def start(self, widget, *args):
        change_start_size = Animation(size_hint=(1, 0.2), duration=1)
        change_start_size.start(widget)
        self.ids['"roomba"'].size_hint = (0.2, 0.2)
        move_left = Animation(
            pos_hint={'center_x': 0.25, 'center_y': 0.7}, duration=2)
        move_left.start(self.ids['"roomba"'])
        self.ids['"left"'].size_hint = (0.0, 0.0)

class Vacuum(App):
    def build(self):
        return MainLayout()


if __name__ == '__main__':
    Vacuum().run()
