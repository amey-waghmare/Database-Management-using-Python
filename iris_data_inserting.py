import mysql.connector
import csv


# Open the File Here
csv.register_dialect('myDialect', delimiter = ',')
file = open("iris.data","r")
print("step 1: IRIS Datafile open here",type(file))
print(file)

data=[]
reader = csv.reader(file)
for row in reader:
    data.append(row)
    #print(row)
print("Step2: Data being added in data list",type(data))
#print(data)



# Creating the database here------------------------------------------------------------EXECUTE ONLY ONCE
#createDatabase = "CREATE DATABASE "

#mydb = mysql.connector.connect(host = "127.0.0.1",port = "3306",user = "amey",passwd = "7241" )#, tls_versions='tls1.2')
#print(mydb)
#mycursor=mydb.cursor()

#databaseName = input("Enter the name of database you wank to create\t")
#databaseName = "iris_dataset"
#querryToCreateDatabase = createDatabase + databaseName
#mycursor.execute(querryToCreateDatabase)

#print("Database Created\nFollowing are the available databases in your MYSQL\n")

#mycursor.execute("SHOW DATABASES")
#for i in mycursor:
#    print(i[0])



# Now start by creating a new table-------------------------------------------------------Execute only once

mydb = mysql.connector.connect(host = "127.0.0.1", port = "3306", user = "amey",passwd = "7241", database = "iris_dataset")
print(mydb)

#mycursor = mydb.cursor()
#mycursor.execute("CREATE TABLE dataset_of_iris_3 (feature1 REAL, feature2 REAL, feature3 REAL, feature4 REAL, name TEXT)")  # THIS PROGRAM CREATES TABLE NAMED data with 5 columns
#print("Step3: A table is created")

mycursor = mydb.cursor()

# EACH ROW IS FIRST TAKEN AND THEN STORED IN DATABASE
for item in data:
    query = "INSERT INTO dataset_of_iris_2 (feature1,feature2,feature3,feature4,name) VALUES (%s,%s,%s,%s,%s);"
    values = tuple(item)
    print("Step4: Values being inserted",values)
    print(type(values))
    mycursor.execute(query, values)
    mydb.commit()
    print(mycursor.rowcount,"Record inserted")


#print("Record insert ID:", mycursor.lastrowid)
