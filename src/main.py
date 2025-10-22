import argparse
from src import api

def display_meal_details(meal: dict):
    """
    Display detailed information about a meal.

    Parameters
    ----------
    meal : dict
        A dictionary containing meal details from TheMealDB API.

    Returns
    -------
    None
        Prints meal information to the console. If `meal` is None, prints an error message.
    """
    if not meal:
        print("Error: Could not retrieve meal details.")
        return

    print(f"\n✨ {meal.get('strMeal', 'Unknown Meal Name')} ✨")
    print("-" * 50)
    print(f"Category: {meal.get('strCategory', 'N/A')} | Cuisine: {meal.get('strArea', 'N/A')}")
    print("\n📝 Ingredients:")
    for i in range(1, 21):
        ingredient = meal.get(f"strIngredient{i}")
        measure = meal.get(f"strMeasure{i}")
        if ingredient and ingredient.strip():
            print(f"- {ingredient} ({measure.strip() if measure else ''})")
    print("\n📖 Instructions:")
    print(meal.get("strInstructions", "No instructions available."))


def main():
    """
    The CLI entry point for TheMealDB application.

    Parses command-line arguments and executes the corresponding subcommand:
    - random: Fetch a random meal
    - search: Search meals by name
    - category: List meals in a category
    - list: List all meal categories
    - details: Get full meal details by ID
    - filter-ingredient: Filter meals by ingredient

    Returns
    -------
    None
        Executes commands and prints results to the console.
    """
    parser = argparse.ArgumentParser(description="TheMealDB CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Random
    subparsers.add_parser("random", help="Get a random meal")

    # Search
    search_parser = subparsers.add_parser("search", help="Search meals by name")
    search_parser.add_argument("name", help="Meal name to search")

    # Category
    category_parser = subparsers.add_parser("category", help="List meals in a category")
    category_parser.add_argument("category", help="Meal category name")

    # List categories
    subparsers.add_parser("list", help="List all meal categories")

    # Details by ID
    details_parser = subparsers.add_parser("details", help="Get full meal details by ID")
    details_parser.add_argument("id", help="Meal ID")

    # Filter by ingredient
    ingredient_parser = subparsers.add_parser("filter-ingredient", help="Filter meals by ingredient")
    ingredient_parser.add_argument("ingredient", help="Ingredient name (e.g., beef)")

    args = parser.parse_args()

    if args.command == "random":
        meal = api.get_random_meal()
        display_meal_details(meal)

    elif args.command == "search":
        meals = api.search_meals_by_name(args.name)
        if meals:
            for meal in meals:
                print(f"{meal['idMeal']}: {meal['strMeal']}")
        else:
            print("No meals found.")

    elif args.command == "category":
        meals = api.get_meals_by_category(args.category)
        if meals:
            for meal in meals:
                print(f"{meal['idMeal']}: {meal['strMeal']}")
        else:
            print("No meals found in this category.")

    elif args.command == "list":
        categories = api.list_categories()
        print("Available categories:")
        for cat in categories:
            print(f"- {cat}")

    elif args.command == "details":
        meal = api.get_meal_by_id(args.id)
        display_meal_details(meal)

    elif args.command == "filter-ingredient":
        meals = api.filter_meals_by_ingredient(args.ingredient)
        if meals:
            for meal in meals:
                print(f"{meal['idMeal']}: {meal['strMeal']}")
        else:
            print("No meals found with this ingredient.")


if __name__ == "__main__":
    main()