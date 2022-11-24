from extract import retrieve_data


def take_item():
    food_item = input("food item: ")
    retrieve_data.get_data(food_item)


if __name__ == '__main__':
    take_item()