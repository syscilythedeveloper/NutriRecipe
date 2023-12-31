
# NutriRecipe



NutriRecipe is a user-friendly application designed to cater to culinary enthusiasts, health-conscious individuals, and anyone seeking culinary inspiration. This app empowers users to discover a world of delicious recipes tailored to their specific preferences. With NutriRecipe, you can effortlessly search for recipes based on desired ingredients, macronutrients, and dietary preferences. The seamless registration feature, allowing users to create an account, save their favorite recipes, and access them with ease. Whether you're a seasoned chef or a cooking novice, NutriRecipe is your go-to companion for culinary exploration and healthy eating.




## Table of Contents

- [Installation](#installation)

## Installation

To run this project locally, you'll need Python and a few Python packages. Here's how to set up your environment:

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/syscilythedeveloper/NutriRecipe.git
   cd your-repo

2. Create a virtual environment(Optional, but recommended)
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate

3. Install Dependencies
pip install -r requirements.txt
Set Up Environment Variables:

4. Create a .env file in the project root directory and add your secret API key. Replace YOUR_API_SECRET_KEY with your actual API secret key from https://api.spoonacular.com/:
API_SECRET_KEY=YOUR_API_SECRET_KEY

5. Database Setup: 
flask db init
flask db migrate
flask db upgrade

6. Run the Application
flask run
Your application will be accessible at http://localhost:5000 by default.




