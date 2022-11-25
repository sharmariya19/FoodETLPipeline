import pandas as pd
from transform import required_data


def transform_data(data, food_item):
    df = pd.DataFrame.from_dict(data['foods'], orient='columns')
    df = df[['fdcId', 'lowercaseDescription', 'foodNutrients', 'foodCategory']]
    df.rename(columns={'fdcId': 'foodId', 'lowercaseDescription': 'description'}, inplace=True)
    required_data.put_data(df, food_item)

