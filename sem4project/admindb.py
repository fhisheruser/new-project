import mysql.connector

import signuppage as sp

class AdminVal():

  
  
  username=sp.SignupPage().signup(isinstance).username
  gemail=sp.SignupPage().signup(isinstance).gemail
  contact=sp.SignupPage().signup(isinstance).contact
  area=sp.SignupPage().signup(isinstance).area
  password=sp.SignupPage().signup(isinstance).password
  

  mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="#lilu@5%",
    database="nature",
    port='3306'
  )

  mycursor = mydb.cursor()

  sql = "INSERT INTO nature.adminsignup (username, email, contact, area, pwd) VALUES (%s, %s, %s, %s, %s)"
  #val = ("bd","b",1,"e","i")
  val = [username,gemail,contact,area,password]
  mycursor.execute(sql, val)

  mydb.commit()

  print(mycursor.rowcount, "record inserted.")


obj=AdminVal()
