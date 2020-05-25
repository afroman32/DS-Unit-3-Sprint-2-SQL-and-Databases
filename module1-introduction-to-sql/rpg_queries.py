import os
import sqlite3

# construct a path to wherever your database exists
#DB_FILEPATH = "chinook.db"
DB_FILEPATH = os.path.join(os.path.dirname(__file__), "rpg_db.sqlite3")

connection = sqlite3.connect(DB_FILEPATH)
connection.row_factory = sqlite3.Row #allow us to reference rows as dictionaries
# print("CONNECTION:", connection)

cursor = connection.cursor()

character_count = "SELECT count(distinct character_id) as character_count FROM charactercreator_character;"
char_subclass = """
            SELECT sum(mage) - sum(necromancer) as mage_count
                ,sum(thief) as thief_count
                ,sum(cleric) as cleric_count
                ,sum(fighter) as fighter_count
                ,sum(necromancer) as necromancer_count


            FROM	(SELECT
                    c.character_id
                    ,c.name as character_name
                    ,count(m.character_ptr_id) as mage
                    ,count(t.character_ptr_id) as thief
                    ,count(cl.character_ptr_id) as cleric
                    ,count(f.character_ptr_id) as fighter
                    ,count(n.mage_ptr_id) as necromancer
                    
                
                FROM charactercreator_character c
                    LEFT JOIN charactercreator_mage m ON m.character_ptr_id = c.character_id
                    LEFT JOIN charactercreator_thief t ON t.character_ptr_id = c.character_id
                    LEFT JOIN charactercreator_cleric cl ON cl.character_ptr_id = c.character_id
                    LEFT JOIN charactercreator_fighter f ON f.character_ptr_id = c.character_id
                    LEFT JOIN charactercreator_necromancer n ON n.mage_ptr_id = c.character_id
                GROUP BY 1
            )
                """
items = """
        SELECT count(item_id) as total_items
            ,sum(weapon) as weapon_count
            ,count(item_id) - sum(weapon) as other_item_count
        FROM(
            SELECT
                armory_item.item_id
                ,count(armory_weapon.item_ptr_id) as weapon
            FROM armory_item
            LEFT JOIN armory_weapon on armory_weapon.item_ptr_id = armory_item.item_id
            GROUP BY 1
            )
        """
weapon_count = "SELECT count(item_ptr_id) as WeaponCount FROM armory_weapon"
non_weapon_count = """

                    """
item_per_char = """
                SELECT 
                c.character_id
                ,c.name as character_name
                , count(distinct inv.item_id) as item_count
                FROM charactercreator_character c
                LEFT JOIN charactercreator_character_inventory inv ON c.character_id = inv.character_id
                GROUP BY 1
                LIMIT 20
                """
weapon_per_char = """
                SELECT 
                c.character_id
                ,c.name as character_name
                --   ,inv.item_id
                --   ,w.item_ptr_id as weapon_id
                ,count(distinct w.item_ptr_id) as weapon_count
                FROM charactercreator_character c
                LEFT JOIN charactercreator_character_inventory inv ON c.character_id = inv.character_id
                LEFT JOIN armory_weapon w ON w.item_ptr_id = inv.item_id
                GROUP BY 1
                LIMIT 20
                """
ave_item = """
            SELECT avg(item_count) as average_items
                
            FROM
                (SELECT 
                c.character_id
                ,c.name as character_name
                , count(distinct inv.item_id) as item_count
                FROM charactercreator_character c
                LEFT JOIN charactercreator_character_inventory inv ON c.character_id = inv.character_id
                GROUP BY 1
            )            
            """
ave_weapon = """
            SELECT avg(weapon_count) as average_weapons
            FROM
                (SELECT 
                c.character_id
                ,c.name as character_name
                --   ,inv.item_id
                --   ,w.item_ptr_id as weapon_id
                ,count(distinct w.item_ptr_id) as weapon_count
                FROM charactercreator_character c
                LEFT JOIN charactercreator_character_inventory inv ON c.character_id = inv.character_id
                LEFT JOIN armory_weapon w ON w.item_ptr_id = inv.item_id
                GROUP BY 1
            )
            """



result = cursor.execute(character_count).fetchall()
result2 = cursor.execute(char_subclass).fetchall()
result3 = cursor.execute(items).fetchall()
result6 = cursor.execute(item_per_char).fetchall()
result7 = cursor.execute(weapon_per_char).fetchall()
result8 = cursor.execute(ave_item).fetchall()
result9 = cursor.execute(ave_weapon).fetchall()

print(f'Total characters: {result[0][0]}\n')
print(f'Characters in each subclass:\n mage: {result2[0][0]}\n thief: {result2[0][1]}\n cleric: {result2[0][2]}\n fighter: {result2[0][3]}\n necromancer: {result2[0][4]}')
print(f'\nTotal items: {result3[0][0]}\n')
print(f'Total weapons: {result3[0][1]}\n')
print(f'Total of non weapon items: {result3[0][2]}\n')
print('Items per character: ')
i=0
for row in result6:
    print(result6[i][1], result6[i][2])
    i+=1
    print("-----")

print('\nWeapons per character:')
i=0
for row in result7:
    print(result7[i][1], result6[i][2])
    i+=1
    print("-----")

print(f'\nAverage items: {result8[0][0]}\n')
print(f'Average Weapons:{result9[0][0]}')
# print("Result", result.row[0])
# for row in result:
#     print(row[0])
#     print(row[1])
#     print("-----")