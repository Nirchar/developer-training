from db import con, cursor


# Add Employee

def add_employee():
    Name = input("Enter Employee Name: ")
    Email = input("Enter Employee Email: ")
    Department = input("Enter Employee Department: ")
    Designation = input("Enter Employee Designation: ")
    Date_of_joining = input("Enter DOj: ")

    sql="""
    INSERT INTO employee(Emp_Name,Email,Department,Designation,DOJ) 
    VALUES (%s, %s, %s, %s, %s)"""

    values = (Name,Email,Department,Designation,Date_of_joining)

    cursor.execute(sql,values)

    con.commit()

    print("Employee Added Successfully")


add_employee();


# View Employee

def view_employee():

    cursor.execute("SELECT * FROM employee")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

view_employee();


# Edit Employee

def edit_employee():

    empID = int(input("Enter Employee ID: "))
    Name = input("Enter Employee Name: ")
    Email = input("Enter Employee Email: ")
    Department = input("Enter Employee Department: ")
    Designation = input("Enter Employee Designation: ")
    Date_of_joining = input("Enter DOj: ")

    sql = """
    UPDATE employee SET 
    Emp_Name = %s,
    Email = %s,
    Department = %s,
    Designation = %s,
    DOJ = %s WHERE Employee_ID = %s"""

    values = (Name, Email, Department, Designation, Date_of_joining, empID)

    cursor.execute(sql,values)

    con.commit()

    print("Updated Successfully")


edit_employee();



def del_employee():

    empID = int(input("Enter Employee ID: "))

    cursor.execute("DELETE FROM employee WHERE Employee_ID = %s", (empID,))
    
    con.commit()

    print("Deleted Successfully")


del_employee();



def search_employee():
    Name = input("Enter Employee Name: ")

    cursor.execute("SELECT * FROM employee WHERE Emp_Name LIKE %s", ('%'+Name+'%',))
    
    rows = cursor.fetchall()

    if rows:
        for row in rows:
            print(row)
    
    else:
        print("Employee Not Found")

search_employee();