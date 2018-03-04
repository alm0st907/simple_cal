import kivy
kivy.require("1.9.0")
 
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.uix.listview import ListItemButton


class ToDoItem(ListItemButton):
    pass

class ListViewLayout(BoxLayout):
    pass


class ToDoListApp(App):
    def build(self):
        return ListViewLayout()

lApp = ToDoListApp()
lApp.run()