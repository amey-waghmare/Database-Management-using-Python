import mysql.connector


createDatabase="CREATE DATABASE "



mydb = mysql.connector.connect(host = "127.0.0.1",port = "3306",user = "amey",passwd = "7241" )#, tls_versions='tls1.2')
print(mydb)
mycursor=mydb.cursor()

databaseName = input("Enter the name of database you wank to create\t")
querryToCreateDatabase = createDatabase + databaseName
mycursor.execute(querryToCreateDatabase)

print("Database Created\nFollowing are the available databases in your MYSQL\n")

mycursor.execute("SHOW DATABASES")
for i in mycursor:
    print(i[0])
