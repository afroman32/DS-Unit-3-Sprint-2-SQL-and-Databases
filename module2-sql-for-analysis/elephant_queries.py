import os
import pandas as pd
import psycopg2
from psycopg2.extras import DictCursor, execute_values
from dotenv import load_dotenv
import json

load_dotenv() # reads the contents of the .env file and adds them to the environment

DB_NAME = os.getenv("DB_NAME", default = "OOPS")
DB_USER = os.getenv("DB_User", default = "OOPS")
DB_PASSWORD = os.getenv("DB_PASSWORD", default = "OOPS")
DB_HOST = os.getenv("DB_HOST", default = "OOPS")

# DB_NAME = 'dhlpnbgt'
# DB_USER = 'dhlpnbgt'
# DB_PASSWORD = 'ATyX_JPySUEgYS8bZ50jL1tk9rGr0dIT'
# DB_HOST = 'arjuna.db.elephantsql.com'

connection = psycopg2.connect(dbname= DB_NAME, user= DB_USER, password= DB_PASSWORD, host= DB_HOST)

print("Connection", type(connection))





cursor = connection.cursor(cursor_factory= DictCursor)
print("CURSOR", type(cursor))


cursor.execute('SELECT * from test_table;')
result = cursor.fetchall()

for row in result:
    print("-------")
    print(type(row))
    print(row)


print("--------------------")
query = f"""
CREATE TABLE IF NOT EXISTS test_table2 (
    id SERIAL PRIMARY KEY,
    name varchar(40) NOT NULL,
    data JSONB
);
"""
print("SQL", query)
cursor.execute(query)

my_dict = {"a": 1, "b": ['dog', 'cat', 42], "c": 'true'}
insertion_query = f'INSERT INTO test_table2 (name, data) VALUES %s'

df = pd.DataFrame([
    ['A rowwwwww', 'null'],
    ['Another row, with JSONNNNN', json.dumps(my_dict)],
    ['Third row', 'null'],
    ['Pandas row', 'null']
])

records = df.to_records(index=False)
result = list(records)
execute_values(cursor, insertion_query, list)

# query the table
print('---------------------')
query = 'SELECT * FROM test_table2;'
print('SQL', query)
cursor.execute(query)
for row in cursor.fetchall():
    print(row)

# actually save the transactions
connection.commit()

cursor.close()
connection.close()
