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
    food_name = [food["name"] for food in spicy_foods]
    return food_name

def get_spiciest_foods(spicy_foods):
    spiciest = [food for food in spicy_foods if food["heat_level"] > 5]
    return spiciest

def print_spicy_foods(spicy_foods):
    formatted_foods = [
        f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}"
        for food in spicy_foods
    ]
    for formatted_food in formatted_foods:
        print(formatted_food)

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for spicy_food in spicy_foods:
        if spicy_food["cuisine"].lower() == cuisine.lower():
            return spicy_food
    return None
 
def print_spiciest_foods(spicy_foods, ):
    spiciest_foods = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest_foods)


def get_average_heat_level(spicy_foods):
    addition = sum(spicy_food['heat_level'] for spicy_food in spicy_foods)
    if len(spicy_foods) > 0:
        return addition / len(spicy_foods)
    else:
        return 0
    
def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
