import mysql.connector
import signuppage as sp

class AdminVal:

  def Val():

    username=sp.SignupPage().signup(isinstance).username
    gemail=sp.SignupPage().signup(isinstance).gemail
    contact=sp.SignupPage().signup(isinstance).contact
    area=sp.SignupPage().signup(isinstance).area
    password=sp.SignupPage().signup(isinstance).password
    confirm_password=sp.SignupPage().signup(isinstance).confirm_password

  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="#lilu@5%",
    database="nature"
  )

  mycursor = mydb.cursor()

  sql = "INSERT INTO nature.localsignup (name, email, contact, location, pwd) VALUES (%s, %s, %s, %s, %s)"
  val = ("Kavi","kavi321", 123,"Thane","abc")
  mycursor.execute(sql, val)

  mydb.commit()

  print(mycursor.rowcount, "record inserted.")
  toast('Successfully Registered!!')

  obj=AdminVal()