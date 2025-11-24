def scale_recipe(recipe, portions):
    return {ingredient: amount * portions for ingredient, amount in recipe.items()}