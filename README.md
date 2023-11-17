# osuTopPlayerData
osu! is a rhythmn game where the objective is to click circles to the beat of music. Performance points (pp) are award to players after completing a map. In osu! there are rankings based on how much pp a player has. Top osu players achieve lots of pp by demonstrating their exceptional talent at the game. Over large time periods the top player leaderboards change and I want to analyze and show just how much the top players in the game have changed from 2017 to 2023.

In this program I used the python library mysql.connector along with pandas to get relevant data from two datasets and answer the following questions:

- What is the average pp value in the top 100 in each year?
- What is the average amount of playcount and hours played in each year?
- How has the country distribution of top players changed from 2017 to 2023?
- Which players in each year had the least amount of hours played and most amount of hours played and the respective rank of those players?
- Which players in 2017 are still in the top 100 in 2023?
- How many top players in 2023 have now surpassed the pp value of Cookiezi who was rank 1 in 2017

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

- Russia ranks first, and the Soviet Union is high on the list as well before they became the Russian federation.

**What is the average amount of playcount and hours played in each year?**

- There are 235 Grandmasters who achieved the title when they were 18 or younger, the youngest age being 13 years old.

**How has the country distribution of top players changed from 2017 to 2023?**

- The first woman GM was Nona Gaprindashvili titled in 1978, although the sample size is small we can infer that women have been titled in more recent years compared to men.

**Which players in each year had the least amount of hours played and most amount of hours played and the respective rank of those players?**

- Taking the average elo of each title year might have skewed the results, as Gary Kasparov was the only titled GM in 1980 with the second highest max Elo rating of all time.

**Which players in 2017 are still in the top 100 in 2023?**

- Only one player has surpassed Garry Kasparob in peak ELO rating, Magnus Carlsen.

**How many top players in 2023 have now surpassed the pp value of Cookiezi who was rank 1 in 2017**