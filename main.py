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

    # Q1
    # Query for pp avg in 2017
    pp_query_2017 = """
    SELECT player_name, performance_points FROM osu_2017_data
    """
    pp_results_2017 = database.results_query(connection, pp_query_2017)
    pd_visualizer(pp_results_2017, ["player name","performance points"])
    
    avg_pp_query_2017 = """
    SELECT AVG(performance_points) FROM osu_2017_data
    """
    avg_pp_query_2017 = database.results_query(connection, avg_pp_query_2017)
    pd_visualizer(avg_pp_query_2017, ["total pp average in 2017"])
 
    # Query for pp avg in 2023
    pp_query_2023 = """
    SELECT player_name, performance_points FROM osu_2023_data
    """
    pp_results_2023 = database.results_query(connection, pp_query_2023)
    pd_visualizer(pp_results_2023, ["player name","performance points"])
    
    avg_pp_query_2023 = """
    SELECT AVG(performance_points) FROM osu_2023_data
    """
    avg_pp_query_2023 = database.results_query(connection, avg_pp_query_2023)
    pd_visualizer(avg_pp_query_2023, ["total pp average in 2023"])

    # Q2
    # Query for avg playcount and playtime in 2017
    play_time_query_2017 = """
    SELECT player_name, play_count, hours FROM osu_2017_data
    """
    play_time_results_2017 = database.results_query(connection, play_time_query_2017)
    pd_visualizer(play_time_results_2017, ["player name", "playcount","hours"])
    
    avg_play_time_query_2017 = """
    SELECT AVG(play_count), AVG(hours) FROM osu_2017_data
    """
    avg_play_time_results_2017 = database.results_query(connection, avg_play_time_query_2017)
    pd_visualizer(avg_play_time_results_2017, ["avg playcount in 2017", "avg hours played in 2017"])

    # # Query for avg playcount and playtime in 2023
    play_time_query_2023 = """
    SELECT player_name, play_count, hours FROM osu_2023_data
    """
    play_time_results_2023 = database.results_query(connection, play_time_query_2023)
    pd_visualizer(play_time_results_2023, ["player name", "playcount","hours"])
    
    avg_play_time_query_2023 = """
    SELECT AVG(play_count), AVG(hours) FROM osu_2023_data
    """
    avg_play_time_results_2023 = database.results_query(connection, avg_play_time_query_2023)
    pd_visualizer(avg_play_time_results_2023, ["avg playcount in 2023", "     avg hours played in 2023"])


def pd_visualizer(results, columns):
    db_results = []
    for result in results:
        result = list(result)
        db_results.append(result)

    df = pd.DataFrame(db_results, columns=columns)
    print(df)


if __name__ == "__main__":
    main()