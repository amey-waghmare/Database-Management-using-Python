import mysql.connector

mydb = mysql.connector.connect(host = "127.0.0.1", port = "3306", user = "amey", passwd = "Amey007@@")
print(mydb)
mycursor=mydb.cursor()
print("Below are the databases available")
mycursor.execute("SHOW DATABASES")
for i in mycursor:
    print(i[0])
mydb.close()

dbname = raw_input("Enter the name of database you want to enter\t")

mydb = mysql.connector.connect(host = "127.0.0.1", port = "3306", user = "amey", passwd = "7241", database = dbname)
mycursor=mydb.cursor()

print("Database "+dbname+" Contains following tables")
mycursor.execute("SHOW TABLES")
for i in mycursor:
    print(i[0])
