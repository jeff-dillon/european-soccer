# Remove records where preferred_foot or overall_rating is not null
# Save file with id, overall_rating, and preferred_foot

import os
import pandas as pd
import sqlite3

# path to the database file - update as needed
db_path = 'data/database.sqlite'

conn = sqlite3.connect(db_path)

# Use the metadata table "sqlite_master" to list the tables in this database
# Ignore any internal tables (they start with 'sqlite')
player_attributes = pd.read_sql("""SELECT id, overall_rating, preferred_foot
                                    FROM player_attributes
                                    WHERE preferred_foot IS NOT NULL
                                        OR overall_rating IS NOT NULL; """, conn)

player_attributes.to_csv('data/player_attributes.csv', index = False)