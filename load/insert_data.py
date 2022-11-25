from load import database

global id


def insert_food(item, description, food_category):
    sql = f"""INSERT INTO food(Item, Description, FoodCategory)
                 VALUES('{item}', '{description}', '{food_category}');"""
    db_obj = database.Database()
    db_obj.connect()
    db_obj.insert_rows(sql)


def food_nutrient(nutrient_id, nutrient_name, amount, unit):
    food_id = get_food_id()
    sql = f"""INSERT INTO food_nutrient(foodid, nutrientid, nutrientname, amount, unit)
                     VALUES({food_id[0]}, {nutrient_id}, '{nutrient_name}',  {amount}, '{unit}');"""
    db_obj = database.Database()
    db_obj.connect()
    db_obj.insert_rows(sql)


def get_food_id():
    sql = f"""SELECT MAX(id) FROM food;"""
    db_obj = database.Database()
    db_obj.connect()
    global id
    id = db_obj.get_id(sql)
    return id




