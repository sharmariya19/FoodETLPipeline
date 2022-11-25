from load import insert_data

required_nutrients = ['Protein', 'Total lipid (fat)', 'Sugars, total including NLEA', 'Calcium, Ca', 'Iron, Fe', 'Cholesterol', 'Energy', 'Carbohydrate, by difference']


def put_food_data(df, food_item):
    insert_data.insert_food(food_item, df['description'][0], df['foodCategory'][0])


def put_nutrients(df, food_id):
    for x in range(0, len(df)):
        if df[x]["nutrientName"] in required_nutrients:
            insert_data.food_nutrient(nutrient_id=df[x]["nutrientId"],
                                      nutrient_name=df[x]["nutrientName"], amount=df[x]["value"], unit=df[x]["unitName"])


def put_data(df, food_item):
    try:
        put_food_data(df, food_item)
        put_nutrients(df["foodNutrients"][0], df['foodId'][0])
    except Exception as e:
        print(e)


