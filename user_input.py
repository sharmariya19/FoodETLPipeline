from extract import retrieve_data
import pandas as pd


def take_item():
    try:
        input_data = pd.read_csv('/Users/apple/code/python/food.csv')
        for index, row in input_data.iterrows():
            food_item = row[0]
            retrieve_data.get_data(food_item)
    except:
        print("Can not find path of file")


if __name__ == '__main__':
    take_item()

