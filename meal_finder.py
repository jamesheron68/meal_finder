import random


def get_preferences():
    """Prompt the user for recipe preferences and validate the input."""
    questions = {
        "cuisine": "What type of cuisine would you like?\n",
        "protein": "What type of protein would you like?\n",
        "time": "How long would you like the cooking to take?\n",
        "cost": "How much would you like the meal to cost?\n",
        "vegetarian": "Would you like the meal to be vegetarian? (Y/N)\n",
        "vegan": "Would you like the meal to be vegan? (Y/N)\n",
    }

    answers = {}

    for attribute, question in questions.items():
        while True:
            answer = input(question)
            # Check that the answer is Y or N for the binary questions
            if attribute in {"vegetarian", "vegan"} and answer.strip().upper() not in {
                "Y",
                "N",
            }:
                print("Please enter either Y or N.")
                continue
            # Check that the input is an integer
            if attribute in {"time", "cost"}:
                try:
                    answer = int(answer)
                except ValueError:
                    print("Please enter a number.")
                    continue

            answers[attribute] = answer
            break

    # Type and format conversion of answers
    for field in {"cuisine", "protein"}:
        answers[field] = answers[field].strip().title()

    answers["vegetarian"] = answers["vegetarian"].strip().upper() == "Y"
    answers["vegan"] = answers["vegan"].strip().upper() == "Y"

    return answers


def filter_recipes(recipes, answers):
    """Filter the original list using the answers from the user and return valid recipes."""
    return [
        recipe
        for recipe in recipes
        if (
            recipe["cuisine"] == answers["cuisine"]
            and recipe["protein"] == answers["protein"]
            and recipe["time"] <= answers["time"]
            and recipe["cost"] <= answers["cost"]
            and recipe["vegetarian"] == answers["vegetarian"]
            and recipe["vegan"] == answers["vegan"]
        )
    ]


def choose_recipe(recipes_filtered):
    """Choose a recipe, if the user is unhappy then show alternates."""
    # Exit if no recipes were found
    if not recipes_filtered:
        print("Sorry, there were no matching recipes!")
        exit()

    random.shuffle(recipes_filtered)

    print(f"There were {len(recipes_filtered)} matching recipes found.\n")

    for recipe in recipes_filtered:
        print(f"Your chosen recipe is:\n{recipe['name']}")

        # Make sure the answer is Yes or No
        while True:
            choice = input("Are you happy with your recipe? (Y/N)\n").strip().lower()

            if choice in {"y", "n"}:
                break

            print("Invalid input. Please enter Y or N")
        # Exit the loop if the user is happy with the recipe
        if choice == "y":
            print(f"Great, enjoy your {recipe['name']}!")
            break
    # If the user runs out of recipes, display a message
    else:
        print("Sorry, there are no recipes left.")


def main():

    answers = get_preferences()

    recipes_filtered = filter_recipes(recipes, answers)

    choose_recipe(recipes_filtered)


recipes = [
    {
        "name": "Chicken Fajitas",
        "cuisine": "Mexican",
        "protein": "Chicken",
        "time": 30,
        "cost": 8,
        "vegetarian": False,
        "vegan": False,
    },
    {
        "name": "Chicken Tikka Masala",
        "cuisine": "Indian",
        "protein": "Chicken",
        "time": 40,
        "cost": 7,
        "vegetarian": False,
        "vegan": False,
    },
    {
        "name": "Beef Lasagne",
        "cuisine": "Italian",
        "protein": "Beef",
        "time": 90,
        "cost": 15,
        "vegetarian": False,
        "vegan": False,
    },
    {
        "name": "Salmon with Risotto",
        "cuisine": "Italian",
        "protein": "Salmon",
        "time": 60,
        "cost": 10,
        "vegetarian": False,
        "vegan": False,
    },
    {
        "name": "Tomato and Mozzarella Gnocchi",
        "cuisine": "Italian",
        "protein": "None",
        "time": 40,
        "cost": 6,
        "vegetarian": True,
        "vegan": False,
    },
    {
        "name": "Baked Potato with Tuna",
        "cuisine": "British",
        "protein": "Tuna",
        "time": 30,
        "cost": 5,
        "vegetarian": False,
        "vegan": False,
    },
    {
        "name": "Salmon Aloo Traybake",
        "cuisine": "Indian",
        "protein": "Salmon",
        "time": 45,
        "cost": 8,
        "vegetarian": False,
        "vegan": False,
    },
    {
        "name": "Spaghetti and Meatballs",
        "cuisine": "Italian",
        "protein": "Beef",
        "time": 30,
        "cost": 7,
        "vegetarian": False,
        "vegan": False,
    },
    {
        "name": "Beef Burgers and Fries",
        "cuisine": "American",
        "protein": "Beef",
        "time": 30,
        "cost": 9,
        "vegetarian": False,
        "vegan": False,
    },
    {
        "name": "Chickpea and Harissa Stew",
        "cuisine": "Morrocan",
        "protein": "None",
        "time": 45,
        "cost": 8,
        "vegetarian": True,
        "vegan": True,
    },
    {
        "name": "Fried Tofu with Chilli",
        "cuisine": "Chinese",
        "protein": "None",
        "time": 25,
        "cost": 10,
        "vegetarian": True,
        "vegan": True,
    },
    {
        "name": "Beans on Toast",
        "cuisine": "British",
        "protein": "None",
        "time": 10,
        "cost": 2,
        "vegetarian": True,
        "vegan": True,
    },
]

if __name__ == "__main__":
    main()
