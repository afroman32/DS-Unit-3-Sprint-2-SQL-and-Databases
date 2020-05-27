import os
import pandas as pd
import psycopg2
from psycopg2.extras import DictCursor, execute_values
from dotenv import load_dotenv

load_dotenv() # reads the contents of the .env file and adds them to the environment

DB_NAME = os.getenv("DB_NAME", default = "OOPS")
DB_USER = os.getenv("DB_User", default = "OOPS")
DB_PASSWORD = os.getenv("DB_PASSWORD", default = "OOPS")
DB_HOST = os.getenv("DB_HOST", default = "OOPS")

DB_FILEPATH = os.path.join(os.path.dirname(__file__), "titanic.csv")
df = pd.read_csv(DB_FILEPATH)

connection = psycopg2.connect(dbname= DB_NAME, user= DB_USER, password= DB_PASSWORD, host= DB_HOST)
cursor = connection.cursor(cursor_factory= DictCursor)

# breakpoint()
query = f"""
DROP TABLE titanic;
CREATE TABLE IF NOT EXISTS titanic (
    id SERIAL PRIMARY KEY,
    survived numpy.int64,
    pclass numpy.int64,
    name varchar (40) NOT NULL,
    sex varchar (40) NOT NULL,
    age numpy.int64,
    siblings_spouses_aboard numpy.int64,
    parents_children_aboard numpy.int64,
    fare numpy.float64
);
"""
print("SQL", query)
cursor.execute(query)

# insertion_query = f'INSERT INTO test_table2 (name, data) VALUES %s'

# records = df.to_records(index=False)
# result = list(records)
# execute_values(cursor, insertion_query, result)

# actually save the transactions
connection.commit()

cursor.close()
connection.close()
exit()

# connection = sqlite3.connect(SQ_FILEPATH)
# connection.row_factory = sqlite3.Rows

insertion_query = f'INSERT INTO test_table2 (name, data) VALUES %s'

records = df.to_dict('records')
list_of_tuples = [{r[0], r[1]} for r in records]
execute_values(cursor, insertion_query, list_of_tuples)

cursor = connection.cursor()