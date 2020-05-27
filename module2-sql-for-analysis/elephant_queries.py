import os
import psycopg2
from psycopg2.extras import DictCursor
from dotenv import load_dotenv
load_dotenv() # reads the contents of the .env file and adds them to the environment

# DB_NAME = os.getenv("DB_NAME", default = "OOPS")
# DB_USER = os.getenv("DB_User", default = "OOPS")
# DB_PASSWORD = os.getenv("DB_PASSWORD", default = "OOPS")
# DB_HOST = os.getenv("DB_HOST", default = "OOPS")

DB_NAME = 'dhlpnbgt'
DB_USER = 'dhlpnbgt'
DB_PASSWORD = 'ATyX_JPySUEgYS8bZ50jL1tk9rGr0dIT'
DB_HOST = 'arjuna.db.elephantsql.com'

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