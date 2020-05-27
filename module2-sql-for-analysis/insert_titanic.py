import os
from sqlalchemy import create_engine
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

df.columns = ['survived', 'pclass', 'name', 'sex', 'age', 'siblings_spouses_aboard', 'parents_children_aboard', 'fare']

print(df.columns)

sql_url = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'
engine = create_engine(sql_url)

df.to_sql('titanic', engine, if_exists='replace')

# cursor.close()
# connection.close()
exit()

# connection = sqlite3.connect(SQ_FILEPATH)
# connection.row_factory = sqlite3.Rows

# insertion_query = f'INSERT INTO test_table2 (name, data) VALUES %s'

# records = df.to_dict('records')
# list_of_tuples = [{r[0], r[1]} for r in records]
# execute_values(cursor, insertion_query, list_of_tuples)

# cursor = connection.cursor()