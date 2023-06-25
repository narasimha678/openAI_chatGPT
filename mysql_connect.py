import mysql.connector

#connect to MySQL server
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "bidshift",
    port = 3306
)

#create a cursor object
mycursor = mydb.cursor()

#execute an SQL query
mycursor.execute("SELECT * FROM mysql.user")

#fetch the results
myresult = mycursor.fetchall()

#print the results
for x in myresult:
  print(x)