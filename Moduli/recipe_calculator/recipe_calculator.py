# recipe_calculator.py
import recipes
import calculator
import math

def scale_recipe(recipe, portions):
    return {ingredient: amount * portions for ingredient, amount in recipe.items()}

def main():
    dish = input("Введите название блюда (паста, салат, бутерброд): ")
    recipe = recipes.get_recipe(dish)

    if recipe is None:
        print("Такого рецепта нет.")
        return

    portions = int(input("Сколько порций вы хотите? "))
    scaled = calculator.scale_recipe(recipe, portions)

    print(f"\nИнгредиенты на {portions} порций:")
    for ingredient, amount in scaled.items():
        print(f"- {ingredient}: {amount} г")

main()