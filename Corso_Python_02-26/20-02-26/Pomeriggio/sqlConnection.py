import mysql.connector as msc

mydb = msc.connect(
    host="localhost",
    user="root"
)
print(mydb)

mycursor = mydb.cursor()
query="show databases"
mycursor.execute(query)
print(mycursor.fetchall())

for x in mycursor:
    print(x[0])
