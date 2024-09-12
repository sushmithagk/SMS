import mysql.connector
connection = mysql.connector.connect(
    host='localhost',
    database='sdp',
    user='root',
    password='root123'
)
if connection.is_connected():
    print("successfully connected to the database")
    
    cursor = connection.cursor()
    create_table_query="""
            CREATE TABLE IF NOT EXISTS students (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(225) NOT NULL,
                age INT,
                gender VARCHAR(10)
            )
            """
    cursor.execute(create_table_query)
    print('Table "students" created successfully.')
    
    insert_query="""
              INSERT INTO students (name,age,gender)
              VALUES(%s, %s, %s)
              """
    students_records=[
                  ('Alice',22,'female'),
                  ('bob',24,'male'),
                  ('charlie',23,'male')
             ]
    cursor.executemany(insert_query,students_records) 
    connection.commit()
    print(f"{cursor.rowcount} records inserted into 'students' table")