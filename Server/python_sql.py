import pyodbc

def read(conn):
    print("Read")
    cursor = conn.cursor()
    cursor.execute("select * from student_details")
    for row in cursor:
        print(row)
    print()
conn = pyodbc.connect("Driver = {ODBC Driver 13 for SQL Server};"
                      "Server=DESKTOP-KSLCGIR;"
                      "Databse=intro;"
                      "Trusted_Connection = yes;")

read(conn)
# create(conn)
# update(conn)
# delete(conn)

conn.close()