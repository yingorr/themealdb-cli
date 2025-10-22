import pytest
from unittest.mock import patch
from src import main

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
def test_main_random_command(mock_random, capsys):
    mock_random.return_value = mock_meal
    main.display_meal_details(mock_meal)
    captured = capsys.readouterr()
    assert "Teriyaki Chicken Casserole" in captured.out
    assert "Ingredients" in captured.out


@patch("src.api.search_meal")
def test_main_search_command(mock_search, capsys):
    mock_search.return_value = [mock_meal]
    meals = main.api.search_meal("Chicken")
    main.display_meal_details(meals[0])
    captured = capsys.readouterr()
    assert "Teriyaki Chicken Casserole" in captured.out


@patch("src.api.list_categories")
def test_main_list_categories_command(mock_list, capsys):
    mock_list.return_value = mock_categories
    categories = main.api.list_categories()
    print("\n".join([c["strCategory"] for c in categories["categories"]]))
    captured = capsys.readouterr()
    assert "Beef" in captured.out
    assert "Chicken" in captured.out

@patch("src.api.get_meals_by_category")
def test_main_search_command(mock_search, capsys):
    mock_search.return_value = [mock_meal]
    meals = main.api.get_meals_by_category("Chicken")
    main.display_meal_details(meals[0])
    captured = capsys.readouterr()
    assert "Teriyaki Chicken Casserole" in captured.out