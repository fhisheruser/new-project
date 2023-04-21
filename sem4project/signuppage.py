from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle
from kivy.uix.screenmanager import ScreenManager, Screen
import mysql.connector


#import localdb
#import admindb
#import voldb


class SignupPage(GridLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            # Set the background color to white
            Color(1, 1, 1, 1)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_rect, pos=self._update_rect)
        self.cols = 2
        self.padding = 40
        self.spacing = 30
        
        
        self.add_widget(Label(text="Username:",color=(0, 0, 0, 1),font_size=25))
        self.username_input = TextInput(multiline=False)
        self.add_widget(self.username_input)

        
        self.add_widget(Label(text="Email:",color=(0, 0, 0, 1),font_size=25))
        self.email_input = TextInput(multiline=False)
        self.add_widget(self.email_input)

        
        self.add_widget(Label(text="Contact_Number:",color=(0, 0, 0, 1),font_size=25))
        self.contact_input = TextInput(multiline=False)
        self.add_widget(self.contact_input)

        
        self.add_widget(Label(text="Area:",color=(0, 0, 0, 1),font_size=25))
        self.area_input = TextInput(multiline=False)
        self.add_widget(self.area_input)

    
        self.add_widget(Label(text="Password:",color=(0, 0, 0, 1),font_size=25))
        self.password_input = TextInput(multiline=False, password=True)
        self.add_widget(self.password_input)

        
        self.add_widget(Label(text="Confirm Password:",color=(0, 0, 0, 1),font_size=25))
        self.confirm_password_input = TextInput(multiline=False, password=True)
        self.add_widget(self.confirm_password_input)

        
        self.signup_button = Button(text="Signup", size_hint=(0.5, 1))
        self.signup_button.bind(on_press=self.signup)
        self.add_widget(self.signup_button)


        #self.add_widget(Label(text="Signup Screen"))
        self.back_button = Button(text="Back to Login", size_hint=(0.5, 1), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.back_button.bind(on_press=self.switch_to_login)
        self.add_widget(self.back_button)
        
    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size
        
    def switch_to_login(self, *args):
        # Switch to the login screen
        self.manager.current = 'loginpage'
        sm = ScreenManager()
        sm.add_widget(SignupScreen(name='signup'))
    def signup(self, instance):
        
        username = self.username_input.text
        gemail = self.email_input.text
        contact = self.contact_input.text
        area = self.area_input.text
        password = self.password_input.text
        confirm_password = self.confirm_password_input.text

        if password != confirm_password:
            print("Passwords do not match")
            return
        else:
            conn=mysql.connector.connect(host='localhost', user='root', password='Lamboveno@2020', database='nature')
            my_cursor=conn.cursor()
            query=("Select * from admindb where Email=%s")
            value=(self.email_input.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exists,please try again using another email")
            else:
                my_cursor.execute("insert into admindb values(%s,%s,%s,%s,%s)",(
                                                                    self.username_input.get(),
                                                                    self.email_input.get(),
                                                                    self.contact_input.get(),
                                                                    self.area_input.get(),
                                                                    self.password_input.get()                                                                    
                                                                                 ))
            conn.commit()
            conn.close()
            messagebox.showinfo("SUCCESS","Registered Successfully")

        
        print(f"Username: {username}")
        print(f"Email: {gemail}")
        print(f"Contact Number: {contact}")
        print(f"Area: {area}")
        print(f"Password: {password}")

        #obj=admindb.AdminVal()
        #obj=localdb.Local()
        #obj=voldb.Vol()


class MyNature(App):

    def build(self):
        return SignupPage()


if __name__ == '__main__':
    MyNature().run()
