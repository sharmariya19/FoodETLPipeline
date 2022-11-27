from load.database import Database


class InsertData:
    @staticmethod
    def insert_food(foodId, item, description, food_category):
        sql = f"""INSERT INTO food(foodId, Item, Description, FoodCategory)
                     VALUES({foodId}, '{item}', '{description}', '{food_category}');"""

        db_obj = Database()
        db_obj.connect()
        db_obj.insert_rows(sql)

    @staticmethod
    def food_nutrient(nutrient_id, amount, unit):
        food_id = get_food_id()
        sql = f"""INSERT INTO food_nutrient(foodid, nutrientid, amount, unit)
                         VALUES({food_id[0]}, {nutrient_id}, {amount}, '{unit}');"""

        db_obj = Database()
        db_obj.connect()
        db_obj.insert_rows(sql)

    @staticmethod
    def nutrients(id, nutrientName):
        sql = f"""INSERT INTO nutrient(ID, nutrientName)
                            VALUES({id}, '{nutrientName}');"""
        db_obj = Database()
        db_obj.connect()
        db_obj.insert_rows(sql)


def get_food_id():
    sql = f"""SELECT MAX(id) FROM food;"""
    db_obj = Database()
    db_obj.connect()
    cur = db_obj.conn.cursor()
    cur.execute(sql)
    foodid = cur.fetchone()
    cur.close()
    db_obj.conn.commit()
    return foodid


