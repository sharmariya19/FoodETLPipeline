class CreateTable:
    @staticmethod
    def create_food_table():
        command = '''CREATE TABLE food(
            ID SERIAL PRIMARY KEY,
            FoodID INT,
            Item VARCHAR(100) NOT NULL,
            Description VARCHAR(100),
            FoodCategory VARCHAR(100)
            );'''

        return command

    @staticmethod
    def create_nutrient_table():
        command = '''CREATE TABLE nutrient(
            ID INT PRIMARY KEY,
            nutrientName VARCHAR(100) NOT NULL
            );'''

        return command

    @staticmethod
    def create_food_nutrient_table():
        command = '''CREATE TABLE food_nutrient(
            ID SERIAL PRIMARY KEY,
            foodID INT,
            nutrientID INT,
            Amount FLOAT,
            Unit VARCHAR(10),
            FOREIGN KEY (foodID) REFERENCES food(ID),
            FOREIGN KEY (nutrientID) REFERENCES nutrient(ID)
            );'''
        return command


def create_tables():
    yield CreateTable.create_food_table()
    yield CreateTable.create_nutrient_table()
    yield CreateTable.create_food_nutrient_table()
