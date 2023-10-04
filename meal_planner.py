import random

# Define a dictionary of meals and their ingredients
meals = {
    'Spaghetti Bolognese': ['spaghetti', 'mince', 'tomatoes', 'onions', 'garlic', 'herbs'],
    'Chicken Curry': ['chicken', 'curry sauce', 'rice'],
    'Chicken and Mushroom Pie': ['chicken', 'mushrooms', 'pastry'],
    'Pizza': ['pizza base', 'tomato sauce', 'cheese', 'toppings'],
    'Chicken and Chips': ['chicken', 'chips', 'salad'],
    'Roast Dinner': ['chicken', 'potatoes', 'vegetables', 'gravy'],
    'Fish and Chips': ['fish', 'chips', 'salad'],
    'Burger and Chips': ['burger', 'bun', 'chips', 'salad'],
    'Pasta Bake': ['pasta', 'cheese', 'tomatoes', 'herbs'],
    'Chicken and Rice': ['chicken', 'rice', 'salad'],
}

def generate_meal_plan(meals):
    # randomly select 1 meal for each day of the week
    meal_plan = {day: random.choice(list(meals.keys())) for day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']}
    return meal_plan

def generate_shopping_list(meal_plan):
    # create a shopping list based on the meal plan
    shopping_list = set()
    for meal in meal_plan.values():
        shopping_list.update(meals[meal])
    return sorted(shopping_list)

def main():
    meal_plan = generate_meal_plan(meals)
    print("Meal Plan:")
    for day, meal in meal_plan.items():
        print(f'{day}: {meal}')

    shopping_list = generate_shopping_list(meal_plan)
    print("\nShopping List:")
    for item in shopping_list:
        print(item)
    
if __name__ == '__main__':
    main()