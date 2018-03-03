from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.checkbox import CheckBox #checkbox import

#not sure which import is actually necessary for my graphics code
#from kivy.graphics.instructions import Instruction
#from kivy.graphics.instructions import Canvas
from kivy.graphics import * #I think this just imports everything?


#not sure what half of this does but its a nice little test file

#widgets are the functionality part of kivy
    #widgets are added in order of the calls in app
        #columns filled left to right in order of the call
        #do a vertical box layout for the todo list style mode
#layouts are the arrangement stuff


class TodoList(GridLayout):

    def __init__(self, **kwargs):
        super(TodoList, self).__init__(**kwargs)
        
        #self.title = "SimplCal"    #this doesnt title the window
        self.cols = 2
        

        self.add_widget(Label(text='Task')) #first
        self.username = TextInput(multiline=False) #first entry second column
        self.add_widget(self.username)

        self.add_widget(Label(text='Due Date'))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)

        self.add_widget(Label(text="test"))
        self.add_widget(Label(text='test2',color=(1,1,0,1))) #assign text color
        
        self.add_widget(CheckBox()) #this allows us to draw a checkbox
        
        #this chunk of code lets us draw and position a window
        with self.canvas:
            Color(r=.2,b=.4,g=.6)
            Rectangle(pos=(0,0),size=(100,100))

        
        
        

class MyApp(App):

    def build(self):
        self.title = "SimplCal" #titling the window
        return TodoList()


if __name__ == '__main__':
    MyApp().run()