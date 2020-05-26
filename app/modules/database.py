import mysql.connector as db
from mysql.connector import Error


def connection_db():
    try:
        connection = db.connect(host='hboueix.fr',
                                database='pycheckers',
                                user='pycheckers',
                                password='hugleojul')
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            return connection, cursor

    except Error as e:
        print("Error while connecting to MySQL", e)


def select(columns, table, options=''):
    query = f"select {columns} from {table} {options};"
    print(f'... : {query}')
    connection, cursor = connection_db()
    cursor.execute(query)
    results = cursor.fetchall() if cursor is not None else 'No results'
    print(results)
    cursor.close()
    connection.close()
    print(f'OK : {query}')
    return results


def insert(table, values):
    query = f"insert into {table} values ({('%s,' * len(values))[:-1]});"
    print(f'... : {query}')
    connection, cursor = connection_db()
    cursor.execute(query, values)
    connection.commit()
    cursor.close()
    connection.close()
    print(f'OK : {query}')


def execute_query(query):
    print(f'... : {query}')
    connection, cursor = connection_db()
    cursor.execute(query)
    cursor.close()
    connection.close()
    print(f'OK : {query}')


# execute_query("drop table User;")
# execute_query("create table user (id INT NOT NULL AUTO_INCREMENT, username CHAR(50), password CHAR(255), PRIMARY KEY (id));")

# insert("user (username, password)", ('hugo', 'password'))
#select('*', 'user')
