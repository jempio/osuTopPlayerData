import db as database
import pandas as pd

def main():
    # hidden password
    pw = ""
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
    SELECT ROUND(AVG(performance_points)) FROM osu_2017_data
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
    SELECT ROUND(AVG(performance_points)) FROM osu_2023_data
    """
    avg_pp_query_2023 = database.results_query(connection, avg_pp_query_2023)
    pd_visualizer(avg_pp_query_2023, ["total pp average in 2023"])

    # Q2
    # Query for avg playcount and playtime in 2017
    play_time_query_2017 = """
    SELECT player_name, play_count, hours FROM osu_2017_data
    """
    play_time_results_2017 = database.results_query(connection, play_time_query_2017)
    pd_visualizer(play_time_results_2017, ["player name", "playcount", "hours"])
    
    avg_play_time_query_2017 = """
    SELECT ROUND(AVG(play_count)), ROUND(AVG(hours)) FROM osu_2017_data
    """
    avg_play_time_results_2017 = database.results_query(connection, avg_play_time_query_2017)
    pd_visualizer(avg_play_time_results_2017, ["avg playcount in 2017", "     avg hours played in 2017"])

    # Query for avg playcount and playtime in 2023
    play_time_query_2023 = """
    SELECT player_name, play_count, hours FROM osu_2023_data
    """
    play_time_results_2023 = database.results_query(connection, play_time_query_2023)
    pd_visualizer(play_time_results_2023, ["player name", "playcount","hours"])
    
    avg_play_time_query_2023 = """
    SELECT ROUND(AVG(play_count)), ROUND(AVG(hours)) FROM osu_2023_data
    """
    avg_play_time_results_2023 = database.results_query(connection, avg_play_time_query_2023)
    pd_visualizer(avg_play_time_results_2023, ["avg playcount in 2023", "     avg hours played in 2023"])

    # Q3
    # Query for varying country representation in 2017
    country_query_2017 = """
    SELECT country, COUNT(*) FROM osu_2017_data
    GROUP BY country
    ORDER BY COUNT(*) desc
    LIMIT 10;
    """
    country_results_2017 = database.results_query(connection, country_query_2017)
    pd_visualizer(country_results_2017, ["country", "number of players"])

    # Query for varying country representation in 2023
    country_query_2023 = """
    SELECT country, COUNT(*) FROM osu_2023_data
    GROUP BY country
    ORDER BY COUNT(*) desc
    LIMIT 10;
    """
    country_results_2023 = database.results_query(connection, country_query_2023)
    pd_visualizer(country_results_2023, ["country", "number of players"])

    # Q4
    # Query for players with the highest and lowest hours played in 2017 w/ their ranks
    # Player with most hours in 2017
    most_hours_query_2017 = """
    SELECT player_name, hours, global_rank 
    FROM osu_2017_data
    ORDER BY hours desc
    LIMIT 1;
    """
    most_hours_result_2017 = database.results_query(connection, most_hours_query_2017)
    pd_visualizer(most_hours_result_2017, ["player name", "hours played", "rank"])

    # Player with least hours in 2017
    least_hours_query_2017 = """
    SELECT player_name, hours, global_rank 
    FROM osu_2017_data
    ORDER BY hours asc
    LIMIT 1;
    """
    least_hours_result_2017 = database.results_query(connection, least_hours_query_2017)
    pd_visualizer(least_hours_result_2017, ["player name", "hours played", "rank"])

    # Query for players with the highest and lowest hours played in 2023 w/ their ranks
    # Player with most hours in 2023
    most_hours_query_2023 = """
    SELECT player_name, hours, global_rank 
    FROM osu_2023_data
    ORDER BY hours desc
    LIMIT 1;
    """
    most_hours_result_2023 = database.results_query(connection, most_hours_query_2023)
    pd_visualizer(most_hours_result_2023, ["player name", "hours played", "rank"])

    # Player with least hours in 2023
    least_hours_query_2023 = """
    SELECT player_name, hours, global_rank 
    FROM osu_2023_data
    ORDER BY hours asc
    LIMIT 1;
    """
    least_hours_result_2023 = database.results_query(connection, least_hours_query_2023)
    pd_visualizer(least_hours_result_2023, ["player name", "hours played", "rank"])

    # Q5
    # Query for players that are still in the top 100 in 2023 from 2017
    remained_as_top_player_query = """
    SELECT osu_2017_data.player_name    
    FROM osu_2017_data
    INNER JOIN osu_2023_data 
        ON osu_2017_data.player_name = osu_2023_data.player_name;
    """ 
    top_player_results = database.results_query(connection, remained_as_top_player_query)
    pd_visualizer(top_player_results, ["player name"])

    # Q6
    # Query to see how many players have passed Cookiezi in pp value in 2017, and how much he has gained since?
    cookiezi_query = """
    SELECT osu_2017_data.player_name, osu_2017_data.performance_points AS performance_points, 
    osu_2023_data.performance_points AS performance_points
    FROM osu_2017_data
    INNER JOIN osu_2023_data ON osu_2017_data.player_name = osu_2023_data.player_name
    WHERE osu_2017_data.player_name = "Cookiezi"; 
    """
    result_cookiezi = database.results_query(connection, cookiezi_query)
    pd_visualizer(result_cookiezi, ["player name", "performance points (2017)", 'peformance points (2023)'])
    

    passed_cookiezi_query = """
    SELECT osu_2023_data.player_name, osu_2023_data.performance_points
    FROM osu_2023_data
    INNER JOIN osu_2017_data 
        ON osu_2023_data.performance_points > osu_2017_data.performance_points
    WHERE osu_2017_data.player_name = "Cookiezi"
    """
    result_passed_cookiezi = database.results_query(connection, passed_cookiezi_query)
    pd_visualizer(result_passed_cookiezi, ["player name", "performance points"])
    

def pd_visualizer(results, columns):
    db_results = []
    for result in results:
        result = list(result)
        db_results.append(result)

    df = pd.DataFrame(db_results, columns=columns)
    print(df)


if __name__ == "__main__":
    main()