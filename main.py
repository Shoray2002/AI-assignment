import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.animation import Animation

Builder.load_file('main.kv')


class MainLayout(Widget):
    def __init__(self, **kwargs):
        super(MainLayout, self).__init__(**kwargs)
        self.animation = None

    def right_toggle(self, toggle):
        if toggle.state == 'down':
            print(self.ids)
        else:
            print('Right toggle is up')
            # self.ids.right.source ='dust.png'

    def left_toggle(self, toggle):
        if toggle.state == 'down':
            print(self.ids)
        else:
            print('left toggle is up')
            # self.ids.right.source ='dust.png'

    def animate(self, widget, *args):
        anim = Animation(size_hint=(1, 0.2), duration=1)
        anim.start(widget)


class Vacuum(App):
    def build(self):
        return MainLayout()


if __name__ == '__main__':
    Vacuum().run()
