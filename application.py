import pandas as pd
from flask import Flask, render_template, url_for
from flask import request, redirect

app = Flask(__name__)


@app.route('/recipes')
def recipes():
    # Read CSV file using Pandas
    df = pd.read_csv('recipes.csv')

    # Convert DataFrame to a dictionary so that it can be passed to the template
    recipes = df.to_dict(orient='records')

    # Render the 'recipes.html' template and pass the recipes data to it
    return render_template('recipes.html', recipes=recipes)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/add-recipe', methods=['GET', 'POST'])
def add_recipe():
    if request.method == 'POST':
        # Handle form submission here and add a new recipe to the CSV file
        return redirect(url_for('recipes'))
    return render_template('add-recipe.html')


if __name__ == '__main__':
    app.run(debug=True)
