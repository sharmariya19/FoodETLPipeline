import requests
import json
from config import setting
from transform import preprocessing


def get_data(food_item):
    try:
        response_api = requests.get(
            f'https://api.nal.usda.gov/fdc/v1/foods/search?&api_key={setting.API_KEY}&query={food_item}')
        data = response_api.text
        data = json.loads(data)
        check_response(data)
        preprocessing.transform_data(data, food_item)
    except Exception as e:
        print(e)



def check_response(data):
    if data['totalPages'] < 1:
        print("Sorry no food item related to this word")



