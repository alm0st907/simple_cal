from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.listview import ListItemButton
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.popup import Popup

class ToDoItem(ListItemButton):
    pass

class ListViewLayout(BoxLayout):
    pass

class BaseGui(GridLayout):
    pass


class BaseGuiApp(App):
    def build(self):
        return BaseGui()


if __name__ == '__main__':
    BaseGuiApp().run()