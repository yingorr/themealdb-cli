import pytest
from unittest.mock import patch
from src import api

mock_meal = {
    "idMeal": "52772",
    "strMeal": "Teriyaki Chicken Casserole",
    "strCategory": "Chicken",
    "strArea": "Japanese",
    "strInstructions": "Some cooking instructions",
    "strIngredient1": "Chicken",
    "strMeasure1": "1 lb",
}

mock_categories = {"categories": [{"strCategory": "Beef"}, {"strCategory": "Chicken"}]}


@patch("src.api.get_random_meal")
def test_get_random_meal(mock_get):
    mock_get.return_value = mock_meal
    result = api.get_random_meal()
    assert result["idMeal"] == "52772"


# Fixed: use existing function
@patch("src.api.get_meals_by_category")
def test_search_meal(mock_search):
    mock_search.return_value = [mock_meal]
    results = api.get_meals_by_category("Chicken")
    assert len(results) == 1
    assert results[0]["idMeal"] == "52772"


@patch("src.api.list_categories")
def test_list_categories(mock_list):
    mock_list.return_value = mock_categories
    results = api.list_categories()
    assert "categories" in results
    assert len(results["categories"]) == 2