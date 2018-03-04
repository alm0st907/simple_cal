from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

class BaseGui(GridLayout):
    pass


class BaseGuiApp(App):
    def build(self):
        return BaseGui()


if __name__ == '__main__':
    BaseGuiApp().run()