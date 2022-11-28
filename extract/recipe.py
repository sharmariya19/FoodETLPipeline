import requests
from bs4 import BeautifulSoup
from load.insert_data import InsertRecipe


def get_link(food_item):
    try:
        url = f"https://www.simplyrecipes.com/search?q={food_item}"
        req = requests.get(url)
        recipes = BeautifulSoup(req.content, "html.parser")
        recipe_link = recipes.find(id="card_1-0").get('href')
        print(recipe_link)
        get_recipe_link(food_item, recipe_link)
    except Exception as e:
        print(f"No recipe found for {food_item}")


def get_recipe_link(food_item, recipe_link):
    req = requests.get(recipe_link)
    res = BeautifulSoup(req.content, "html.parser")
    if res.find(id="section--instructions_1-0"):
        print("found")
    else:
        recipe_link = res.find(id="mntl-card-list-items_1-0").get('href')
        req = requests.get(recipe_link)
        res = BeautifulSoup(req.content, "html.parser")
    get_recipe(food_item, res)


def get_recipe(food_item, res):
    get_recipe = res.find_all("span", class_="mntl-sc-block-subheading__text")
    recipe = ""
    for step in get_recipe:
        recipe += step.text[:-2]
    print(f"Recipe of {food_item}: {recipe}")

    InsertRecipe.insert_recipe(food_item, recipe[:-1])


