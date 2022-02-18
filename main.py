import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.animation import Animation

# importing the kivy style sheet
Builder.load_file('main.kv')


class MainLayout(Widget):
    def __init__(self, **kwargs):
        super(MainLayout, self).__init__(**kwargs)
        self.right_flag = False
        self.left_flag = False
        locs = [0.75, 0.25]
        self.ids['"roomba"'].pos_hint['center_x'] = locs[random.randint(0, 1)]
        # starting the roomba in a random location
    # handling the right toggle event

    def right_toggle(self, toggle):
        if toggle.state == 'down':
            self.ids['"right"'].size_hint = (0.5, 0.5)
            self.right_flag = True
            toggle.text='🧹 Remove Salt'
        else:
            self.ids['"right"'].size_hint = (0, 0)
            self.right_flag = False
            toggle.text='🧂 Add Salt'
    # handling the left toggle event

    def left_toggle(self, toggle):
        if toggle.state == 'down':
            self.ids['"left"'].size_hint = (0.5, 0.5)
            self.left_flag = True
            toggle.text='🧹 Remove Salt'
        else:
            self.ids['"left"'].size_hint = (0, 0)
            self.left_flag = False
            toggle.text='🧂 Add Salt'

    # handling the start event
    def start(self, widget, *args):
        change_start_size = Animation(size_hint=(1, 0.2), duration=1)
        change_start_size.start(widget)
        self.ids['"roomba"'].size_hint = (0.2, 0.2)
        self.determine()

    # logic for determining the movement of the roomba
    def determine(self):
        move_left = Animation(
            pos_hint={'center_x': 0.25, 'center_y': 0.7}, duration=2)
        move_right = Animation(
            pos_hint={'center_x': 0.75, 'center_y': 0.7}, duration=2)
        if (self.ids['"roomba"'].pos_hint['center_x'] > 0.5):
            if (self.right_flag):
                self.ids['"right"'].size_hint = (0.0, 0.0)
                self.right_flag = False
                self.ids['"right_toggle"'].state = 'normal'
                # if the roomba is in the right half of the screen and the right button is pressed
            # the roomba will move to the left
            move_left.bind(on_complete=self.edge_cases)
            move_left.start(self.ids['"roomba"'])

        else:
            if (self.left_flag):
                self.ids['"left"'].size_hint = (0.0, 0.0)
                self.left_flag = False
                self.ids['"left_toggle"'].state = 'normal'
                # if the roomba is in the left half of the screen and the left button is pressed
            # the roomba will move to the right
            move_right.bind(on_complete=self.edge_cases)
            move_right.start(self.ids['"roomba"'])

# logic for determining the working of the roomba after the movement
    def edge_cases(self, *args):
        if (self.right_flag):
            self.ids['"right"'].size_hint = (0.0, 0.0)
            self.right_flag = False
            self.ids['"right_toggle"'].state = 'normal'
        if (self.left_flag):
            self.ids['"left"'].size_hint = (0.0, 0.0)
            self.left_flag = False
            self.ids['"left_toggle"'].state = 'normal'


class Vacuum(App):
    def build(self):
        return MainLayout()


if __name__ == '__main__':
    Vacuum().run()
