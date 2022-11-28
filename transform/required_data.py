from load.insert_data import InsertData
from transform import nutrients


def put_food(df, food_item):
    print("food item: ", food_item, "description: ", df['description'][0], "food category: ", df['foodCategory'][0])
    InsertData.insert_food(df['foodId'][0], food_item, df['description'][0], df['foodCategory'][0])


def put_food_nutrients(df):
    for data in range(0, len(df)):
        if df[data]["nutrientName"] in nutrients.required_nutrients:
            InsertData.food_nutrient(nutrient_id=df[data]["nutrientId"], amount=df[data]["value"], unit=df[data]["unitName"])


def put_nutrients(df):
    for nutrient in df:
        if nutrient['nutrientName'] in nutrients.required_nutrients:
            InsertData.nutrients(nutrient['nutrientId'], nutrient["nutrientName"] )


def put_data(df, food_item):
    try:
        put_nutrients(df["foodNutrients"][0])
    except:
        pass
    put_food(df, food_item)
    put_food_nutrients(df["foodNutrients"][0])


