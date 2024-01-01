import mysql.connector
from mysql.connector import Error

create_osu_player_2017_table = """
CREATE TABLE osu_2017_data(
global_rank int, 
country_rank int,
player_name varchar(255),
country varchar(255),
accuracy float(4),
play_count int,
level int,
hours int,
performance_points int,
ranked_score bigint,
ss int,
s int,
a int,
watched_by int,
total_hits int,
device varchar(255)
);
"""

create_osu_player_2023_table = """
CREATE TABLE osu_2023_data(
global_rank int, 
player_name varchar(255),
country varchar(255),
accuracy float(4),
play_count int,
performance_points int,
ss int,
s int,
a int,
level int,
hours int,
watched_by int
);
"""

def create_connection_to_server(host, user, password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = host,
            user = user, 
            password = password
        )
        print("Connection Successful")
    except Error as err:
        print(f"Error: {err}")
    return connection

def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute("DROP DATABASE IF EXISTS top_osu_player")
        cursor.execute(query)
        print("Database Created Successfully")
    except Error as err:
        print(f"Error: {err}")


def create_connection_to_db(host, user, password, db):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = host,
            user = user, 
            password = password, 
            database = db
        )
        print("SQL Database Connection Successful")
    except Error as err:
        print(f"Error: {err}")
    return connection

def populate_2017_player_data(connection, data):
    cursor = connection.cursor()
    cursor.execute("select database();")
    cursor.fetchone()
    cursor.execute('DROP TABLE IF EXISTS osu_2017_data;')
    cursor.execute(create_osu_player_2017_table)
    connection.commit()
    for _, row in data.iterrows():
        sql = "INSERT INTO top_osu_player.osu_2017_data VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        try:
            cursor.execute(sql, tuple(row))
        except Error as err:
            print(f"Error: {err}")
        connection.commit()


def populate_2023_player_data(connection, data):
    cursor = connection.cursor()
    cursor.execute("select database();")
    cursor.fetchone()
    cursor.execute('DROP TABLE IF EXISTS osu_2023_data;')
    cursor.execute(create_osu_player_2023_table)
    connection.commit()
    for _, row in data.iterrows():
        sql = "INSERT INTO top_osu_player.osu_2023_data VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        try:
            cursor.execute(sql, tuple(row))
        except Error as err:
            print(f"Error: {err}")
        connection.commit()

def results_query(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    return result