from load.database import Database


class InsertData:
    @staticmethod
    def create_connection(sql):
        db_obj = Database()
        db_obj.connect()
        db_obj.insert_rows(sql)

    @staticmethod
    def insert_food(foodId, item, description, food_category):
        sql = f"""INSERT INTO food(foodId, Item, Description, FoodCategory)
                     VALUES({foodId}, '{item}', '{description}', '{food_category}');"""
        InsertData.create_connection(sql)

    @staticmethod
    def food_nutrient(nutrient_id, amount, unit):
        food_id = get_food_id()
        sql = f"""INSERT INTO food_nutrient(foodid, nutrientid, amount, unit)
                         VALUES({food_id[0]}, {nutrient_id}, {amount}, '{unit}');"""

        InsertData.create_connection(sql)

    @staticmethod
    def nutrients(id, nutrientName):
        sql = f"""INSERT INTO nutrient(ID, nutrientName)
                            VALUES({id}, '{nutrientName}');"""
        InsertData.create_connection(sql)


class InsertRecipe():
    def insert_recipe(item, recipe):
        sql = f"""INSERT INTO recipe(Item, Recipe)
                                 VALUES('{item}', '{recipe}');"""

        InsertData.create_connection(sql)


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
