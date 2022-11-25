

def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = [
        '''CREATE TABLE food(
        ID SERIAL PRIMARY KEY,
        FoodID INT,
        Item VARCHAR(100) NOT NULL,
        Description VARCHAR(100),
        FoodCategory VARCHAR(100)
        );'''
        ,
        '''CREATE TABLE food_nutrient(
        ID SERIAL PRIMARY KEY,
        foodID INT,
        nutrientID INT,
        nutrientName VARCHAR(50),
        Amount FLOAT,
        Unit VARCHAR(10),
        FOREIGN KEY (foodID) REFERENCES food(ID)
        );'''
    ]
    return commands

