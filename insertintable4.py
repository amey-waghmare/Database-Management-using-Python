import mysql.connector
import csv


mydb = mysql.connector.connect(host = "127.0.0.1", port = "3306", user = "amey",passwd = "7241", database = "new_database")
print(mydb)

mycursor=mydb.cursor()

# TO SHOW AVAILABLE TABLES IN DATABASE
mycursor.execute("SHOW TABLES")
for i in mycursor:
    print(i)

data=[]
csv.register_dialect('myDialect', delimiter = ',')
file = open("dataFile.txt","r")
print("step 1: Datafile open here",type(file))
print(file)

reader = csv.reader(file)
for row in reader:
    data.append(row)
    #print(row)
print("Step2: Data being added in data list",type(data))
print(data)

# EACH ROW IS FIRST TAKEN AND THEN STORED IN DATABASE
for item in data:
    query="INSERT INTO data (col1,col2,col3,col4,col5) VALUES (%s,%s,%s,%s,%s)"
    values=(item)
    print("Step3: Values being inserted",values)
    print(type(values))
    mycursor.execute(query,values)
    mydb.commit()
    print(mycursor.rowcount,"Record inserted")


print("Record insert ID:", mycursor.lastrowid)
