import mysql.connector

cnx = None
def create_or_connect_to_db(usersql,passsql,hostsql):
    global cnx
    if cnx is not None:
        return cnx
    
    # Define the database configuration
    config = {
        'user': usersql,
        'password': passsql,
        'host': hostsql,
        'raise_on_warnings': True
        }
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()

    """
    The double asterisk ** before config in the mysql.connector.connect() function call is
    a special syntax in Python that allows passing a dictionary as a set of keyword arguments
    to a function. This means that the key-value pairs in the config dictionary are unpacked 
    and passed to the mysql.connector.connect() function as separate arguments, 
    as if they were specified as user=xxx, password=yyy, .... 
    This allows for a more concise and readable way of passing multiple arguments to a function.
    """
   
    database_name = input('Enter your database name: ')

        # Check if the database already exists
    cursor.execute("SHOW DATABASES LIKE '{}'".format(database_name))
    result = cursor.fetchone()

        # If the database doesn't exist, create it
    if not result:
            cursor.execute("CREATE DATABASE {}".format(database_name))
            print("Database created successfully.")
    else:
            print("Database already exists.")

        # Connect to the database
    cnx.database = database_name
    print("Connected to database: {}".format(database_name))

        # Close the cursor and return the connection object
    cursor.close()
    return cnx

cnx = create_or_connect_to_db('root', 'pass', 'localhost')
