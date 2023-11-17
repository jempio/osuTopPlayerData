# main.py
import db as db
import pandas as pd

def main():
    # hidden password
    pw = "-Chubbynuts7757"
    osu_2017_data = pd.read_csv('data\osu_2017_player_data.csv', index_col=False, delimiter=",")
    osu_2023_data = pd.read_csv('data\osu_2023_player_data.csv', index_col=False, delimiter=",")
    connection = db.create_connection_to_server("localhost", "jempio", pw)
    create_top_osu_player_db_query = "CREATE database top_osu_player"
    db.create_database(connection, create_top_osu_player_db_query)

    connection = db.create_connection_to_db("localhost", "jempio", pw, "top_osu_player")
    db.populate_2017_player_data(connection, osu_2017_data)
    db.populate_2023_player_data(connection, osu_2023_data)

    country_query = """
    SELECT country, COUNT(*) FROM osu_2017_data
    GROUP BY country
    ORDER BY COUNT(*) DESC
    """
    country_results = db.results_query(connection, country_query)
    pd_visualizer(country_results, ["country", "number_players"])

    country_query = """
    SELECT country, COUNT(*) FROM osu_2023_data
    GROUP BY country
    ORDER BY COUNT(*) DESC
    """
    country_results = db.results_query(connection, country_query)
    pd_visualizer(country_results, ["country", "number_players"])

def pd_visualizer(results, columns):
    from_db = []
    for result in results:
        result = list(result)
        from_db.append(result)

    df = pd.DataFrame(from_db, columns=columns)
    print(df)


if __name__ == "__main__":
    main()