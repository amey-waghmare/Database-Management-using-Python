import mysql.connector

mydb = mysql.connector.connect(host = "127.0.0.1", port = "3306", user = "amey", passwd = "7241", database = "new_database")
print(mydb)

mycursor=mydb.cursor()
mycursor.execute("CREATE TABLE data (col1 INT,col2 INT,col3 INT, col4 INT, col5 INT)")  # THIS PROGRAM CREATES TABLE NAMED data with 5 columns
