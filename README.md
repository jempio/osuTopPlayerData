# osuTopPlayerData
osu! is a rhythmn game where the objective is to click circles to the beat of music. Performance points (pp) are award to players after completing a map. In osu! there are rankings based on how much pp a player has. Top osu players achieve lots of pp by demonstrating their exceptional talent at the game. Over large time periods the top player leaderboards change and I want to analyze and show just how much the top players in the game have changed from 2017 to 2023.

In this program I used the python library mysql.connector along with pandas to get relevant data from two datasets and answer the following questions:

- What is the average pp value for the top 100 players in each year?
- What is the average amount of playcount and hours played in each year?
- How has the country distribution of top players changed from 2017 to 2023?
- Which players in each year had the least amount of hours played and most amount of hours played and the respective rank of those players?
- Which players in 2017 are still in the top 100 in 2023?
- How many top players in 2023 have now surpassed the pp value of Cookiezi who was rank 1 in 2017?

## Data
Two Data files were used in this project, credit is given below.

### Osu Top Player Data in 2017
- Author: Svidon
- https://www.kaggle.com/datasets/svidon/osurankings

### Osu Top Player Data in 2023
- Author: Julliane Pierre
- https://www.kaggle.com/datasets/jullianepierre/osu-standard-rankings

## Results
Results from the SQL queries were all put into panda dataframes and printed to console, which are displayed below.

**What is the average pp value in the top 100 in each year?**

- In 2017, the average pp value is shown to be 10127.
- In 2023, it has shot up to 16854.

**What is the average amount of playcount and hours played in each year?**

- In 2017, the average play count is 98569 plays, and the average amount of hours played in the top 100 was 1283 hours.
- Now in 2023, the average play count is 159052 plays, and the average amount of hours played in the top 100 is 2172 hours. 

**How has the country distribution of top players changed from 2017 to 2023, what are the top 3 countries with the most representation?**

- In 2017, the countries with the most players in the top 100 was the United States, South Korea, and a three way tie between France, Germany and Japan with 14, 13, and 7 players representing their countries resepctively 
- In 2023, the countries with the most players in the top 100 was the United States, Australia, and a four way tie between Canada, Poland, Russian Federation and South Korea, with 22, 7, and 6 players representing their countries resepctively.
- The United States continues to have the most top players representing in the top 100 and increased this number by 8 since 2017.

**Which players in each year had the least amount of hours played and most amount of hours played and the respective rank of those players?**

- In 2017, the player with the most hours played was WubWoofWolf with 4104 hours played. This player was rank 35 at this time.
- The player with the least hours played was 1E308, more commonly known today as Nameless Player, with 269 hours played. This player was rank 90 at this time.
- In 2023, the player with the most hours played was Varvalian with 4571 hours played. This player was rank 21 at this time.
- The player with the least hours played was sakuraskip, with 269 hours played. This player was rank 59 at this time.

**Which players in 2017 are still in the top 100 in 2023?**

- These 7 players are still in the top 100 in 2023.
- Players such as idke, RyuK, Aricin, would also be here but due to name changes, this dataset is unable to account for them. In addition due to inactivity, players like Vaxei, and Bubbleman would also be present on this list.

**How many top players in 2023 have now surpassed the pp value of Cookiezi who was rank 1 in 2017 and how much pp has he gained since?**

- Every single player in the top 100 in 2023 have surpassed the pp value held by rank 1 Cookiezi in 2017
- Additionally, Cookiezi himself remains in the top 100 and has increased his pp value by 4013.