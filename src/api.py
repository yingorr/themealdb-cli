import requests

BASE_URL = "https://www.themealdb.com/api/json/v1/1/"

def get_random_meal():
    """
    Fetch a random meal from TheMealDB API.

    Returns
    -------
    dict or None
        A dictionary containing meal details if successful, otherwise None.
    """
    try:
        resp = requests.get(f"{BASE_URL}random.php")
        resp.raise_for_status()
        data = resp.json()
        return data.get("meals", [None])[0]
    except requests.RequestException:
        print("Network error occurred.")
        return None
    except ValueError:
        print("Error decoding JSON.")
        return None

def search_meals_by_name(name: str):
    """
    Search for meals by their name.

    Parameters
    ----------
    name : str
        The name or partial name of the meal to search for.

    Returns
    -------
    list of dict or None
        A list of meal dictionaries matching the search, or None if no meals found or an error occurs.
    """
    try:
        resp = requests.get(f"{BASE_URL}search.php", params={"s": name})
        resp.raise_for_status()
        data = resp.json()
        return data.get("meals")
    except requests.RequestException:
        print("Network error occurred.")
        return None
    except ValueError:
        print("Error decoding JSON.")
        return None

def get_meal_by_id(meal_id: str):
    """
    Get full meal details by ID.

    Parameters
    ----------
    meal_id : str
        The ID of the meal to fetch.

    Returns
    -------
    dict or None
        A dictionary of meal details if found, otherwise None.
    """
    try:
        resp = requests.get(f"{BASE_URL}lookup.php", params={"i": meal_id})
        resp.raise_for_status()
        data = resp.json()
        meals = data.get("meals")
        if not meals:
            print(f"No meal found with ID {meal_id}.")
            return None
        return meals[0]
    except requests.RequestException:
        print("Network error occurred.")
        return None
    except ValueError:
        print("Error decoding JSON.")
        return None

def get_meals_by_category(category: str):
    """
    Get meals filtered by category.

    Parameters
    ----------
    category : str
        The category of meals to fetch.

    Returns
    -------
    list of dict or None
        A list of meals in the given category, or None if an error occurs.
    """
    try:
        resp = requests.get(f"{BASE_URL}filter.php", params={"c": category})
        resp.raise_for_status()
        data = resp.json()
        return data.get("meals")
    except requests.RequestException:
        print("Network error occurred.")
        return None
    except ValueError:
        print("Error decoding JSON.")
        return None

def filter_meals_by_ingredient(ingredient: str):
    """
    Filter meals by ingredient.

    Parameters
    ----------
    ingredient : str
        The ingredient to filter meals by.

    Returns
    -------
    list of dict or None
        A list of meals containing the ingredient, or None if an error occurs.
    """
    try:
        resp = requests.get(f"{BASE_URL}filter.php", params={"i": ingredient})
        resp.raise_for_status()
        data = resp.json()
        return data.get("meals")
    except requests.RequestException:
        print("Network error occurred.")
        return None
    except ValueError:
        print("Error decoding JSON.")
        return None

def list_categories():
    """
    List all available meal categories.

    Returns
    -------
    list of str
        A list of category names. Returns an empty list if an error occurs.
    """
    try:
        resp = requests.get(f"{BASE_URL}categories.php")
        resp.raise_for_status()
        data = resp.json()
        categories = [c["strCategory"] for c in data.get("categories", [])]
        return categories
    except requests.RequestException:
        print("Network error occurred.")
        return []
    except ValueError:
        print("Error decoding JSON.")
        return []