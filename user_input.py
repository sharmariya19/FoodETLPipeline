from extract import retrieve_data, recipe
import pandas as pd


class InputData:
    @staticmethod
    def read_item():
        input_data = input("Enter a item: ")
        retrieve_data.get_data(input_data)
        InputData.recipe(input_data)

    @staticmethod
    def read_csv():
        try:
            input_data = pd.read_csv('/Users/apple/code/python/food.csv')
            for index, row in input_data.iterrows():
                food_item = row[0]
                retrieve_data.get_data(food_item)
                InputData.recipe(food_item)
        except:
            print("Can not find path of file")

    @staticmethod
    def recipe(food_item):
        recipe.get_link(food_item)

