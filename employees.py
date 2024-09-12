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
            CREATE TABLE IF NOT EXISTS employees (
                id INT  PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                position VARCHAR(100),
                salary DECIMAL(10,2) NOT NULL,
                department VARCHAR(100)
              )
            """
    cursor.execute(create_table_query)
    print('Table "employees" created successfully.')

    insert_query="""
            INSERT INTO employees (id, name, position, salary, department)
            VALUES(%s, %s, %s,%s,%s)
            """
    employees_records=[
              (1, 'John Doe', 'Software Engineer', 60000.00, 'IT'),
              (2, 'Jane Smith', 'Project Manager', 75000.00, 'Management'),
              (3, 'Mike Johnson', 'DevOps Engineer', 70000.00, 'IT'),   
             ]

    cursor.executemany(insert_query,employees_records) 
    connection.commit()
    print(f'{cursor.rowcount} records inserted into "employees" table')
