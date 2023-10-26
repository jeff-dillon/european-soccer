import os
import pandas as pd
import sqlite3

# path to the database file - update as needed
db_path = 'data/database.sqlite'

conn = sqlite3.connect(db_path)

# Remove records where preferred_foot or overall_rating is not null
# Only select one row per player based on highest rating
# convert birthday to birth month (Jan, Feb, etc.)
# Save file with id, overall_rating, birth_month, and preferred_foot
player_attributes = pd.read_sql("""SELECT player_attributes.player_fifa_api_id AS 'id', 
                                            preferred_foot,
                                            CASE strftime('%m', player.birthday) 
                                                WHEN '01' THEN 'Jan'
                                                WHEN '02' THEN 'Feb'
                                                WHEN '03' THEN 'Mar'
                                                WHEN '04' THEN 'Apr'
                                                WHEN '05' THEN 'May'
                                                WHEN '06' THEN 'Jun'
                                                WHEN '07' THEN 'Jul'
                                                WHEN '08' THEN 'Aug'
                                                WHEN '09' THEN 'Sep'
                                                WHEN '10' THEN 'Oct'
                                                WHEN '11' THEN 'Nov'
                                                WHEN '12' THEN 'Dec'
                                                ELSE '' END as 'birth_month',
                                            max(overall_rating) AS 'overall_rating'
                                    FROM player_attributes
                                        LEFT JOIN player on player_attributes.player_fifa_api_id = player.player_fifa_api_id
                                    WHERE preferred_foot IS NOT NULL
                                        OR overall_rating IS NOT NULL
                                    GROUP BY player_attributes.player_fifa_api_id, preferred_foot; """, conn)

player_attributes.to_csv('data/player_attributes.csv', index = False)