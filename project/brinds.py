#!C:\Python312\python.exe
import cgi
import mysql.connector

print("content-type:\n\r\n\r")
print("<html>")
print("<body>")

form=cgi.FieldStorage()

fullname=form.getvalue("fullname","")
email=form.getvalue("email","")
phone=form.getvalue("phone","")
dob=form.getvalue("dob","")
password=form.getvalue("password","")
gender=form.getvalue("gender","")
address=form.getvalue("address","")

print(f"<center><h2>Registration Details<br><br>"
      f"Name:{fullname}<br><br>"
      f"Email id:{email}<br><br>"
      f"Phone No:{phone}<br><br>"
      f"Date of Birth:{dob}<br><br>"
      f"Password:{password}<br><br>"
      f"Gender:{gender}<br><br>"
      f"Address:{address}<br><br>"
      f"</center>"
      f"</h2>")

db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="login"
)
cursor=db.cursor()
sql="INSERT INTO data(name,mail,number,Dob,pass,genDer,addresss) VALUES(%s,%s,%s,%s,%s,%s,%s)"
val=(fullname,email,phone,dob,password,gender,address)
cursor.execute(sql,val)
db.commit()


print("</body>")
print("</html>")