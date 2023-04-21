import kivy
from kivy.app import App

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.graphics import Color, Rectangle
from kivy.uix.screenmanager import ScreenManager, Screen
from adminlogin import AdminPage
from coworkerlogin import CoworkerPage
kivy.require('1.11.1')


class LoginPage(BoxLayout):

    def adminpage(self,instance):
        
        
        self.orientation = 'vertical'
        self.spacing = 20
        self.padding = 50

        self.title = Label(text='Admin Login', font_size=30, halign='center')
        self.add_widget(self.title)

        self.username = TextInput(hint_text='Username', font_size=20, size_hint=(None, None), size=(400, 50), pos_hint={'center_x': 0.5})
        self.add_widget(self.username)

        self.password = TextInput(hint_text='Password', password=True, font_size=20, size_hint=(None, None), size=(400, 50), pos_hint={'center_x': 0.5})
        self.add_widget(self.password)

        self.error_label = Label(text='', font_size=20, color=(1, 0, 0, 1), halign='center')
        self.add_widget(self.error_label)

        self.login_button = Button(text='Login', font_size=20, size_hint=(None, None), size=(200, 50), pos_hint={'center_x': 0.5})
        #self.login_button.bind(on_press=self.check_credentials)
        self.add_widget(self.login_button)
        #.opacity = 0

    def coworker(self,instance):
        self.orientation = 'vertical'
        self.spacing = 20
        self.padding = 50

        self.title = Label(text='Co-worker Login', font_size=30, halign='center')
        self.add_widget(self.title)

        self.username = TextInput(hint_text='Username', font_size=20, size_hint=(None, None), size=(400, 50), pos_hint={'center_x': 0.5})
        self.add_widget(self.username)

        self.password = TextInput(hint_text='Password', password=True, font_size=20, size_hint=(None, None), size=(400, 50), pos_hint={'center_x': 0.5})
        self.add_widget(self.password)

        self.error_label = Label(text='', font_size=20, color=(1, 0, 0, 1), halign='center')
        self.add_widget(self.error_label)

        self.login_button = Button(text='Login', font_size=20, size_hint=(None, None), size=(200, 50), pos_hint={'center_x': 0.5})
        #self.login_button.bind(on_press=self.check_credentials)
        self.add_widget(self.login_button)

    

    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas:
            # Set the background color to white
            Color(1, 1, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)

        self.bind(size=self._update_rect, pos=self._update_rect)
        self.orientation = 'vertical'
        self.spacing = 20
        self.padding = 50

        self.background = Image(source=r'logo.png', keep_ratio=False,size_hint=(1, 5))
        self.add_widget(self.background)

        

        self.username = TextInput(hint_text='Username', font_size=20)
        self.add_widget(self.username)

        self.password = TextInput(hint_text='Password', password=True, font_size=20)
        self.add_widget(self.password)

        self.buttons_layout = BoxLayout(orientation='horizontal', spacing=20, size_hint_y=None, height=50)
        self.add_widget(self.buttons_layout)

        self.admin_button = Button(text='Admin', font_size=20)
        self.admin_button.bind(on_press=self.adminpage )
        self.buttons_layout.add_widget(self.admin_button)
        #.opacity = 0

        self.coworkers_button = Button(text='Co-workers', font_size=20)
        self.coworkers_button.bind(on_press=self.coworker )
        self.buttons_layout.add_widget(self.coworkers_button)

        self.locals_button = Button(text='Locals', font_size=20)
        self.locals_button.bind(on_press=self.locals_login)
        self.buttons_layout.add_widget(self.locals_button)

        self.signup_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=50)
        self.add_widget(self.signup_layout)

        self.new_here_label = Label(text="New here? Create an account", font_size=20, color=(0, 0, 0, 1))
        self.signup_layout.add_widget(self.new_here_label)

        #self.signup_button = Button(text='SIGN UP', font_size=20)
        #self.signup_layout.add_widget(self.signup_button)



      
        self.signup_button = Button(text="Signup",font_size=30, pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.signup_button.bind(on_press=self.switch_to_signup)
        self.add_widget(self.signup_button)
    
    def switch_to_signup(self, *args):
        # Switch to the signup screen
        self.manager.current = 'signup'
        
        


        
    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size
    def admin_login(self, instance):
        username = self.username.text
        password = self.password.text

        if username == 'admin' and password == 'password':
            self.title.text = 'Admin Login Successful'
        else:
            self.title.text = 'Invalid Username or Password'

    def coworkers_login(self, instance):
        username = self.username.text
        password = self.password.text

        if username == 'coworker' and password == 'password':
            self.title.text = 'Co-workers Login Successful'
        else:
            self.title.text = 'Invalid Username or Password'

    def locals_login(self, instance):
        username = self.username.text
        password = self.password.text

        if username == 'local' and password == 'password':
            self.title.text = 'Locals Login Successful'
        else:
            self.title.text = 'Invalid Username or Password'

   

class MyApp(App):
    def build(self):
         
        return LoginPage()


if __name__ == '__main__':
    MyApp().run()

    
