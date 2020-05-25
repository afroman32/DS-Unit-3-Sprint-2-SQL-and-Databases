import pandas as pd
import os
import sqlite3

DB_FILEPATH = os.path.join(os.path.dirname(__file__), "buddymove_holidayiq.csv")
SQ_FILEPATH = os.path.join(os.path.dirname(__file__), "buddymove_holidayiq.sqlite3")
df = pd.read_csv(DB_FILEPATH)

connection = sqlite3.connect(SQ_FILEPATH)
connection.row_factory = sqlite3.Row

cursor = connection.cursor()

df.to_sql('review', con= connection, if_exists= 'replace')

row = "SELECT count(Sports) as rows FROM review"
print(f'Number of rows: {cursor.execute(row).fetchall()[0][0]}')

reviews = """
        SELECT 
            count(distinct Nature) as reviews_over_100

        FROM 
            (SELECT 
                'User Id'
                ,Nature
                ,Shopping

            FROM review
            Where  Nature >= 100
            -- Where Shopping >=100
            GROUP BY 3
            )
            WHERE Shopping >=100
        """
over100 = cursor.execute(reviews).fetchall()

print(f'Number of users who reviewed over at least 100 in Nature and Shopping: {over100[0][0]}')
