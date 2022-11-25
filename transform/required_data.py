from load import insert_data

required_nutrients = ['Protein', 'Total lipid (fat)', 'Sugars, total including NLEA', 'Calcium, Ca', 'Iron, Fe', 'Cholesterol', 'Energy', 'Carbohydrate, by difference']


def put_food_data(df, food_item):
    print(df['foodId'][0], food_item, df['description'][0], df['foodCategory'][0])
    insert_data.insert_food(df['foodId'][0], food_item, df['description'][0], df['foodCategory'][0])


def put_nutrients(df, food_id):
    for x in range(0, len(df)):
        if df[x]["nutrientName"] in required_nutrients:
            print(food_id, df[x]["nutrientId"] , df[x]["value"])
            insert_data.food_nutrient(food_id=food_id, nutrient_id=df[x]["nutrientId"],
                                      nutrient_name=df[x]["nutrientName"], amount=df[x]["value"], unit=df[x]["unitName"])


def put_data(df, food_item):
    put_food_data(df, food_item)
    put_nutrients(df["foodNutrients"][0], df['foodId'][0])

