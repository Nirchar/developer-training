import mysql.connector

con = mysql.connector.connect(
    host = "localhost", 
    user = "root", 
    password = "Curricode#26", 
    database = "employee_db"
    )

cursor = con.cursor()