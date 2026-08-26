# Meal Finder

A small Python project that recommends recipes based on the user's preferences.

This project was built as a **Python learning exercise**, with a focus on practising functions, dictionaries, lists, loops, conditionals, input validation, list comprehensions, and basic error handling.

## What It Does

The program asks the user for a set of recipe preferences:

* Cuisine
* Protein
* Maximum cooking time
* Maximum cost
* Vegetarian preference
* Vegan preference

It then:

1. Validates the user's input.
2. Filters the available recipes based on their preferences.
3. Randomly selects a matching recipe.
4. Gives the user the option to accept the recipe or see another.
5. Continues until the user accepts a recipe or runs out of matching recipes.

### Example

```text
What type of cuisine would you like?
Italian

What type of protein would you like?
Beef

How long would you like the cooking to take?
60

How much would you like the meal to cost?
10

Would you like the meal to be vegetarian? (Y/N)
N

Would you like the meal to be vegan? (Y/N)
N

There were 1 matching recipes found.

Your chosen recipe is:
Spaghetti and Meatballs

Are you happy with your recipe? (Y/N)
Y

Great, enjoy your Spaghetti and Meatballs!
```

## Python Concepts Practised

### Functions

The program is broken into separate functions, each with a specific responsibility:

* `get_preferences()` — collects and validates user input.
* `filter_recipes()` — finds recipes matching the user's preferences.
* `choose_recipe()` — randomly presents matching recipes and handles the user's choice.
* `main()` — controls the overall program flow.

This helped me practise breaking a program into smaller, reusable pieces rather than putting everything into one block of code.

### Dictionaries

Recipes are represented using dictionaries:

```python
{
    "name": "Chicken Fajitas",
    "cuisine": "Mexican",
    "protein": "Chicken",
    "time": 30,
    "cost": 8,
    "vegetarian": False,
    "vegan": False,
}
```

The user's answers are also stored in a dictionary.

### Lists

The collection of recipes is stored as a list of dictionaries, allowing the program to iterate over and filter multiple recipes.

### List Comprehensions

The recipe filtering uses a list comprehension:

```python
[
    recipe
    for recipe in recipes
    if ...
]
```

This was useful practice for filtering data in Python.

### Loops

`for` and `while` loops are used to:

* Ask questions.
* Validate input.
* Iterate through recipes.
* Allow the user to keep trying different recipes.

### Input Validation

The program checks that:

* Vegetarian and vegan answers are either `Y` or `N`.
* Cooking time and cost are valid integers.
* The recipe acceptance question receives either `Y` or `N`.

Invalid input causes the program to ask the question again rather than continuing with bad data.

### Data Cleaning / Formatting

User input is cleaned before being used:

```python
answers[field] = answers[field].strip().title()
```

and:

```python
answers["vegetarian"] = answers["vegetarian"].strip().upper() == "Y"
```

This means inputs such as `mexican` or `y` can still be converted into the expected format.

### Randomisation

The `random` module is used to shuffle the matching recipes:

```python
random.shuffle(recipes_filtered)
```

This prevents the same recipe from always being presented first.

## Project Structure

At the moment, the project is contained in a single Python file:

```text
recipe-recommender/
│
├── recipe_recommender.py
└── README.md
```

The recipes are currently hard-coded into the Python script.

## How to Run

Make sure Python is installed, then run:

```bash
python recipe_recommender.py
```

No external packages are required. The project only uses Python's built-in `random` module.

## Current Limitations

This is intentionally a small learning project, so there are several limitations.

* Recipes are hard-coded rather than stored in a database or external file.
* The user must provide an exact cuisine and protein match.
* There are only a small number of recipes.
* There is no recipe information such as ingredients or cooking instructions.
* Cost is represented as a simple integer rather than a real currency value.
* There is currently no way to add or remove recipes through the program.
* The program exits if no matching recipes are found.

## Future Improvements

Some possible improvements as I continue learning Python:

* Move recipes into a CSV or JSON file.
* Allow the user to leave some preferences blank.
* Improve the matching system so that similar preferences can still produce results.
* Add ingredients and cooking instructions.
* Allow the user to add their own recipes.
* Add a "favourite recipe" feature.
* Improve error handling.
* Separate the recipe data from the application logic.
* Add automated tests with `pytest`.
* Add more sophisticated recipe recommendation logic.
* Eventually connect the project to a database.

## What I'm Learning

The main purpose of this project is not to build a sophisticated recipe recommendation engine. It is to learn by **building something practical from scratch**.

The project is helping me understand how individual Python concepts fit together to create a complete program, particularly:

**Input → Validation → Data → Filtering → Logic → Output**

Future versions will be used to gradually introduce more advanced Python concepts and improve the project as my skills develop.
