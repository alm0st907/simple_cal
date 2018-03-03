import kivy
import os
from kivy.app import App
from kivy.uix.label import Label
#print(kivy.__version__)
kivy.require('1.10.0')
os.environ['KIVY_GL_BACKEND'] = "sdl2"




class MyApp(App):

    def build(self):

        #either way is valid syntax
        #MyApp.title = "My Window" #titles the window
        self.title = "My Window"
        
        return Label(text="Hello World") #middle screen text

if __name__ == '__main__':
    MyApp().run()
