import mysql.connector
import loginpage as lp
from loginpage import LoginPage
    

class Val():

    #get email and password from Screen
    username=LoginPage().admin_login().username
    password=LoginPage().admin_login().password

    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="#lilu@5%",
    database="nature"
    )

    cursor = mydb.cursor()
            #run query to check email/password
        query = "SELECT count(*) FROM volsignup where email='"+username+"' and pwd='"+password+"'"
        cursor.execute(query)
        data = cursor.fetchone()
        count = data[0]
                #verif login/email
                #if invalid
        if count == 0:
                toast('Invalid Login/Password')
                #else, if valid
        else:
            toast('Login and Password are correct!')
                
            mydb.commit()
            mydb.close()
            pass

class MyApp(App):
    def build(self):
        return LoginPage()


if __name__ == '__main__':
    MyApp().run()