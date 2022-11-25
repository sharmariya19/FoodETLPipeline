from load import database


def insert_food(food_id, item, description, food_category):
    sql = f"""INSERT INTO food(ID, Item, Description, FoodCategory)
                 VALUES({food_id}, '{item}', '{description}', '{food_category}');"""
    print("a")
    db_obj = database.Database()
    print("B")
    db_obj.connect()
    print("c")
    db_obj.insert_rows(sql)
    print("d")


def food_nutrient(food_id, nutrient_id,nutrient_name, amount, unit):
    sql = f"""INSERT INTO food_nutrient(foodid, nutrientid, nutrientname, amount, unit)
                     VALUES({food_id}, {nutrient_id}, '{nutrient_name}',  {amount}, '{unit}');"""
    db_obj = database.Database()
    db_obj.connect()
    db_obj.insert_rows(sql)





