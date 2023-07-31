import pandas as pd

# Create dictionary with recipes
data = {
    "Recipe Name": ["Lasagna", "Pizza", "Burger"],
    "Image Link": ["lasagna.jpg", "pizza.jpg", "burger.jpg"],
    "Ingredients": [
        "Pasta, Tomato Sauce, Cheese, Mushrooms, Ground Beef",
        "Pizza Dough, Tomato Sauce, Cheese, Pepperoni",
        "Burger Bun, Patty, Lettuce, Tomato, Cheese",
    ],
    "Preparation Instructions": [
        "Layer the tomato sauce, cheese, mushrooms, and ground beef between the pasta, bake for 30 minutes at 375F",
        "Spread tomato sauce and cheese on pizza dough, add pepperoni, bake for 15 minutes at 425F",
        "Grill patty, place between burger buns with lettuce, tomato, and cheese",
    ],
    "Serving Instructions": ["Serves 3-4 people", "Serves 2-3 people", "Serves 1 person"],
}

# Create DataFrame
df = pd.DataFrame(data)

# Save DataFrame to csv file
df.to_csv('recipes.csv', index=False)
