# Project Name: TheMealDB CLI (Recipe Assistant)

## Overview
A professional command-line tool to help users find recipes, get random meal ideas, and browse by category using TheMealDB API. This project was developed with AI assistance to simulate a real-world, collaborative software development workflow.

## API Integration
- **API:** TheMealDB (Recipe Database)
- **Base URL:** `https://www.themealdb.com/api/json/v1/1/`
- **Authentication:** Uses the test API key `'1'` embedded in the base URL, so no API keys are required for setup or execution.
- **Key Endpoints:**
    - `/random.php` — Get a single random meal with full details.
    - `/search.php?s={meal_name}` — Search for meals by name.
    - `/filter.php?i={ingredient}` — Filter meals by main ingredient.
    - `/categories.php` — Get a list of all meal categories.
- **Data Format:** API responses are JSON. Meal data is typically found under the `'meals'` key, while category data appears under `'categories'`. Each meal object includes up to 20 ingredients (`strIngredient1` → `strIngredient20`) and corresponding measures (`strMeasure1` → `strMeasure20`).

## CLI Commands
The CLI’s entry point is `python -m src.main`, implemented using `argparse` with subcommands.

- **`meal random`** — Fetch and display a random meal with full recipe details (name, category, ingredients, and instructions).  
- **`meal search [name]`** — Search for meals by name (e.g., “chicken”) and list meal names and their corresponding IDs.  
- **`meal details [id]`** — Display full details of a meal by ID (ingredients, measures, instructions).  
- **`meal categories`** — List all available meal categories in a clean, readable format.  
- **`meal filter-ingredient [ingredient]`** — Filter and list all meals containing a specific ingredient.  

## Technical Stack
- **Language:** Python 3.10+
- **CLI Framework:** `argparse` — for command parsing and structured subcommands.
- **HTTP Client:** `requests` — for all API interactions.
- **Testing:** `pytest` — for automated test discovery and execution.
- **Mocking:** `unittest.mock` — used to mock API responses (`requests.get`) in unit tests.
- **CI/CD:** GitHub Actions — runs automated tests on every push or pull request.

## Code Organization
- **`src/main.py`** — CLI entry point, sets up argument parsing, subcommands, and output display logic.  
- **`src/api.py`** — Handles all HTTP requests to TheMealDB API. Manages endpoint URLs, responses, and error handling.  
- **`src/utils.py`** *(optional but recommended)* — Helper functions to format and display meal data, such as pairing ingredients and measures.  
- **`tests/test_api.py`** — Unit tests for `src/api.py`, fully mocked to avoid live API calls.  
- **`tests/test_main.py`** — Tests for CLI logic and output formatting.

## Standards & Constraints
- **Code Style:** Follows PEP 8 guidelines for clean and readable Python code.  
- **Documentation:** Every public function and class includes clear docstrings explaining its purpose, parameters, and return values.  
- **Error Handling:**  
  - Catches `requests.exceptions.RequestException` for network issues.  
  - Handles `json.JSONDecodeError` if the API returns invalid JSON.  
  - Gracefully manages cases where `'meals'` or `'categories'` are `None` (no results).  
- **Testing Requirements:**  
  - All network calls must be mocked — no real HTTP requests during testing.  
  - Each command and API function must have at least one unit test ensuring proper behavior and error handling.

## AI Assistance Summary
This project was developed with AI assistance in:
1. **Project Planning:** Selecting TheMealDB API and defining core CLI functionality.  
2. **Architecture Design:** Outlining the folder structure and defining modular code organization.  
3. **Documentation:** Creating structured `README.md`, `AGENTS.md`, and CI/CD templates.  
4. **Testing Strategy:** Designing pytest cases and mock-based test isolation.  
5. **Best Practices:** Ensuring clean code style, error handling, and automation alignment with modern Python development workflows.
