# I think it was easier to get the rpg data uploaded to MongoDB
import os
import sqlite3
import pymongo
from dotenv import load_dotenv

load_dotenv()

# connect to sqlite
DB_FILEPATH = os.path.join(os.path.dirname(__file__), ".." , "module1-introduction-to-sql", "rpg_db.sqlite3")

connection = sqlite3.connect(DB_FILEPATH)
connection.row_factory = sqlite3.Row #allow us to reference rows as dictionaries
# print("CONNECTION:", connection)

cursor = connection.cursor()

# connect to mongo
DB_USER = os.getenv("MONGO_USER", default="OOPS")
DB_PASSWORD = os.getenv("MONGO_PASSWORD", default="OOPS")
CLUSTER_NAME = os.getenv("MONGO_CLUSTER_NAME", default="OOPS")



connection_url = f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{CLUSTER_NAME}.mongodb.net/test?retryWrites=true&w=majority"
print("----------------")
print("URI:", connection_url)

client = pymongo.MongoClient(connection_url)

db = client.rpg
db.armory_item.drop()
db.armory_weapon.drop()
db.charactercreator_character.drop()
db.charactercreator_character_inventory.drop()
db.charactercreator_cleric.drop()
db.charactercreator_fighter.drop()
db.charactercreator_mage.drop()
db.charactercreator_necromancer.drop()
db.charactercreator_thief.drop()

# docs_count = {}
docs = []
# insert charactercreator_character table
collection = db.charactercreator_character
query = "SELECT * FROM charactercreator_character" 
result = cursor.execute(query).fetchall()

i = 0
for row in result:
    collection.insert_one({
        'character_id': result[i][0],
        'name': result[i][1],
        'level': result[i][2],
        'exp': result[i][3],
        'hp': result[i][4],
        'strength': result[i][5],
        'intelligence': result[i][6],
        'dexterity': result[i][7],
        'wisdrom': result[i][8]
    })
    i+=1
# print('charactercreator_character', collection.count_documents({}))


# insert charactercreator_character_inventory
collection = db.charactercreator_character_inventory
query = "SELECT * FROM charactercreator_character_inventory" 
result = cursor.execute(query).fetchall()

i = 0
for row in result:
    collection.insert_one({
        'id': result[i][0],
        'character_id': result[i][1],
        'item_id': result[i][2]
    })
    i+=1
# print('charactercreator_character_inventory', collection.count_documents({}))


# insert charactercreator_cleric table
collection = db.charactercreator_cleric
query = "SELECT * FROM charactercreator_cleric" 
result = cursor.execute(query).fetchall()

i = 0
for row in result:
    collection.insert_one({
        'character_ptr_id': result[i][0],
        'using_shield': result[i][1],
        'mana': result[i][2]
    })
    i+=1
# print('charactercreator_cleric', collection.count_documents({}))


# insert charactercreator_fighter table
collection = db.charactercreator_fighter
query = "SELECT * FROM charactercreator_fighter" 
result = cursor.execute(query).fetchall()

i = 0
for row in result:
    collection.insert_one({
        'character_ptr_id': result[i][0],
        'using_shield': result[i][1],
        'rage': result[i][2]
    })
    i+=1
# print('charactercreator_fighter', collection.count_documents({}))


# insert charactercreator_mage table
collection = db.charactercreator_mage
query = "SELECT * FROM charactercreator_mage" 
result = cursor.execute(query).fetchall()

i = 0
for row in result:
    collection.insert_one({
        'character_ptr_id': result[i][0],
        'has_pet': result[i][1],
        'mana': result[i][2]
    })
    i+=1
# print('charactercreator_mage', collection.count_documents({}))


# insert charactercreator_necromancer table
collection = db.charactercreator_necromancer
query = "SELECT * FROM charactercreator_necromancer" 
result = cursor.execute(query).fetchall()

i = 0
for row in result:
    collection.insert_one({
        'mage_ptr_id': result[i][0],
        'talisman_charged': result[i][1]
    })
    i+=1
# print('charactercreator_necromancer', collection.count_documents({}))


# insert charactercreator_thief table
collection = db.charactercreator_thief
query = "SELECT * FROM charactercreator_thief" 
result = cursor.execute(query).fetchall()

i = 0
for row in result:
    collection.insert_one({
        'character_ptr_id': result[i][0],
        'is_sneaking': result[i][1],
        'energy': result[i][2]
    })
    i+=1


# insert armory_item into mongo
collection = db.armory_item
query = "SELECT * FROM armory_item" 
result = cursor.execute(query).fetchall()

i = 0
for row in result:
    collection.insert_one({
        'item_id': result[i][0],
        'name': result[i][1],
        'value': result[i][2],
        'weight': result[i][3],
    })
    i+=1


# inseert armory_weapon table
collection = db.armory_weapon
query = "SELECT * FROM armory_weapon" 
result = cursor.execute(query).fetchall()

i = 0
for row in result:
    collection.insert_one({
        'item_ptr_id': result[i][0],
        'power': result[i][1]
    })
    i+=1


print("COLLECTIONS:", db.list_collection_names())