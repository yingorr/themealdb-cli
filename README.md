# Recipe CLI

A command-line interface (CLI) application that allows users to explore meals and recipes from around the world using a public recipe API. Users can fetch random meals, search meals by category, list available categories, and view detailed meal information.

---

## Features

- Fetch a **random meal** with full details (ingredients, measurements, instructions).  
- **Search meals** by category.  
- **List all available categories**.  
- View **detailed meal information** in a clean, readable format.

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/recipe-cli.git
cd recipe-cli
```

2. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # Windows: `venv\Scripts\activate`
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

### Random Meal

```bash
python -m src.main random
```

### Search Meals by Category

```bash
python -m src.main category Chicken
```

### List Categories

```bash
python -m src.main list
```

### View Meal Details by ID

```bash
python -m src.main details 52772
```

---

## API Information

This project uses [TheMealDB API](https://www.themealdb.com/api.php) for meal and recipe data.

---

## Testing

Run all tests with `pytest`:

```bash
PYTHONPATH=$(pwd) pytest -v tests/
```

---

## Technologies

- Python 3.8+  
- argparse  
- requests  
- pytest  
- unittest.mock  

---

## Badges
![Tests](https://github.com/yingorr/is4010-yingorr-labs/actions/workflows/tests.yml/badge.svg)

![License](https://img.shields.io/badge/license-MIT-blue)