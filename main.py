import db as database
import pandas as pd

def main():
    pw = "-Chubbynuts7757"
    osu_2017_data = pd.read_csv('data/osu_2017_player_data.csv', index_col=False, delimiter=",")
    osu_2023_data = pd.read_csv('data/osu_2023_player_data.csv', index_col=False, delimiter=",")
    connection = database.create_connection_to_server("localhost", "jempio", pw)
    create_top_osu_player_db_query = "CREATE DATABASE top_osu_player"
    database.create_database(connection, create_top_osu_player_db_query)
    connection = database.create_connection_to_db("localhost", "jempio", pw, "top_osu_player")
    database.populate_2017_player_data(connection, osu_2017_data)
    database.populate_2023_player_data(connection, osu_2023_data)

def pd_visualizer(results, columns):
    db_results = []
    for result in results:
        result = list(result)
        db_results.append(result)

    df = pd.DataFrame(db_results, columns=columns)
    print(df)


if __name__ == "__main__":
    main()