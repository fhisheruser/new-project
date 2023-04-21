import kivy
from kivy.app import App
from kivy.config import Config
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.textinput import TextInput
from kivy.metrics import dp
##from kivy.uix.image import Image
from mynaturedetail import ProfilePage
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen

from profile import ProfilePage
import time
kivy.require('1.9.1')

##from kivy.uix.camera import Camera



##kivy.require('2.0.0')

class about(Screen):
    pass

class navbar1(Screen):
 



    def profile(self, instance):
        self.orientation = 'vertical'
        self.padding = [50, 50]
        #header = BoxLayout(size_hint=(1, 1.5))
        #header.add_widget(Label(text='My Profile', font_size=30, bold=True,color=[0, 0, 0, 1]))
        #self.add_widget(header)

        # Create content with profile image, name, and bio
        content = BoxLayout(orientation='vertical', padding=(10, 20))
        button = Button(text='back',size_hint = (0.06, 0.06),pos_hint ={'x':0, 'y':0.93})
        button.bind(on_press=self.__init__)
        self.add_widget(button)
        
          # Create the profile image widget
        self.profile_image = Image(source='profileimage.png', size_hint=(None, None), size=(200, 200),pos_hint={'center_x': 0.5})
        self.profile_image.allow_stretch = True
        self.profile_image.keep_ratio = False
        self.profile_image.center_x = self.center_x
        self.profile_image.center_y = self.top - 100
      
        self.add_widget(self.profile_image)

        # Create name label and text input
        name_label = Label(text='Name:', font_size=24, bold=True,color=[0, 0, 0, 1])
        name_input = TextInput(text='', font_size=30,size_hint=(1, 0.1))
        content.add_widget(name_label)
        content.add_widget(name_input)

        # Create bio label and text input
        bio_label = Label(text='Bio:', font_size=24, bold=True,color=[0, 0, 0, 1])
        bio_input = TextInput(text='', font_size=30,size_hint=(1, 0.1))
        content.add_widget(bio_label)
        content.add_widget(bio_input)

        # Create button to upload profile image
        upload_button = Button(text='Upload Profile Image', font_size=15,size_hint=(1, 0.2))
        content.add_widget(upload_button)

        # Add content to profile page
        self.add_widget(content)
        #self.spacing = 20
        #self.padding = 20
##    def capture(self,instance):
##         return Camera(play=True)
##         
    def __init__(self, **kwargs):
        super(navbar1, self).__init__(**kwargs)
##        with self.canvas:
            # Set the background color to white
##            Color(1, 1, 1)
##            self.rect = Rectangle(size=self.size, pos=self.pos)
##            self.bind(size=self._update_rect, pos=self._update_rect)
##      
##        
##            self.orientation = 'vertical'
##            self.padding = 20
##            self.spacing = 10
##            
        #button=Boxlayout(orientation = 'horizontal',size_hint = (1, None),height = 50)
        button = Button(text='back',size_hint = (0.06, 0.06),pos_hint ={'x':0, 'y':0.93})
        #button.bind(on_press=self)
        self.add_widget(button)
        

        # Set the size of the BoxLayout to the size of the parent widget
       
        
        #welcome_label = Label(text='Welcome to Naturalistic!',color=(0, 0, 0, 1), font_size=10, size_hint=(1, 0.3))
        #self.add_widget(welcome_label)

        #description_label = Label(text='The App will provide ',color=(0, 0, 0, 1), font_size=20, size_hint=(1, 0.5))
        #self.add_widget(description_label)
        

        button_row = BoxLayout(orientation='horizontal', size_hint=(1, 0.07))

        about_button = Button(text='About')
        home_button = Button(text='Home')
##        camera_button = Button(text='Camera')
##        camera_button.bind(on_press=self.capture)
        profile_button = Button(text='Profile')
        profile_button.bind(on_press=self.profile)

        about_button.pos_hint = {'center_x': 0.9, 'center_y': 1}
        home_button.pos_hint = {'center_x': 1.2, 'center_y': 1}
        camera_button.pos_hint = {'center_x': 1.5, 'center_y': 1}
        profile_button.pos_hint = {'center_x': 1.8, 'center_y': 1}

        button_row.add_widget(about_button)
        button_row.add_widget(home_button)
       ## button_row.add_widget(camera_button)
        button_row.add_widget(profile_button)

        self.add_widget(button_row)

    
            
    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    pass

        
class MyApp(App):
   
    def build(self):
        return super().build()

    def all_kv_files(self):
        Builder.load_file('libs/screens/navbar1.kv')

if __name__ == '__main__':
    MyApp().run()
