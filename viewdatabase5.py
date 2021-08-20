import mysql.connector
import csv


mydb = mysql.connector.connect(host = "127.0.0.1", port = "3306", user = "amey", passwd = "7241", database = "new_database")     # TYPE DATABASE WHICH WE WANT TO SEE
mycursor = mydb.cursor()

#SAVING DATA IN FILE BELOW
file=open("fromdatabase.txt","w")
writer=csv.writer(file,delimiter=",")
data=[]


mycursor.execute("SELECT * FROM data")                 # THIS IS THE NAME OF TABLE data
result = mycursor.fetchall()
count=0                                # USE fetchone() for first row of table in database
for i in result:
    print(i)
    data.append(i)
    writer.writerow(i)
    count=count+1

print("Above is the data in the given tabel")

mycursor.execute("SELECT COUNT(col1) FROM data")
result1=mycursor.fetchone()
print("Total number of datapoints are",result1)
print(i)
file.close()


# TO SEE SOME ELEMENTS AND NOT ALL ELEMENTS, UNCOMMENT THE CODE BELOW

#mycursor.execute("SELECT * FROM data WHERE col1 LIKE '990'")                         # THIS IS NOT FOR STRONG EQUALITY BUT FOR SIMILARITY
mycursor.execute("SELECT * from data WHERE col4 = '144'")
result = mycursor.fetchall()
for i in result:
    print("The result of last query is \n",i)
