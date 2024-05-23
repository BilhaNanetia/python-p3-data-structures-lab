spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    '''Returns a list of names for each spicy food.'''
    return [food["name"] for food in spicy_foods]


def get_spiciest_foods(spicy_foods):
    '''Returns a list of dicts for food with heat level greater than 5.'''
    return [food for food in spicy_foods if food["heat_level"] > 5]


def print_spicy_foods(spicy_foods):
    '''Prints spicy food formatted with 🌶  emojis.'''
    for food in spicy_foods:
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")
    

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    '''Returns a dict for spicy food that matches a cuisine.'''
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
        

def print_spiciest_foods(spicy_foods):
    '''Prints spicy foods with heat level greater than 5.'''
    for food in get_spiciest_foods(spicy_foods):
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")

def get_average_heat_level(spicy_foods):
    '''Returns average of heat levels in spicy_foods.'''
    return sum([food["heat_level"] for food in spicy_foods]) / len(spicy_foods)

def create_spicy_food(spicy_foods, spicy_food):
    '''Returns original list of spicy_foods with new spicy_food added.'''
    spicy_foods.append(spicy_food)
    return spicy_foods
