"""Seed file to make sample data for pets db."""

from models import User, Recipe, FavoriteRecipe, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

user1 = User(username='Sydney123', password='12345')
user2 = User(username='Teresa123', password='12345')
user3 = User(username='Syscily123', password='12345')


# Add new objects to session, so they'll persist
db.session.add_all([user1, user2, user3])


# Commit--otherwise, this never gets saved!
db.session.commit()

"""
recipe1=Recipe(title='turkeywings', link='turkeyhut.org')
recipe2=Recipe(title='chittlerings', link='highbloodpressure.org')
recipe3=Recipe(title='lamb', link='lammylammylamb.org')

db.session.add([recipe1, recipe2, recipe3])
db.session.commit()
"""

veggielovers = Recipe(title='tomatoes', link = 'madeupveglink.com',savedrecipes=[FavoriteRecipe(user_id=user1.id),
FavoriteRecipe(user_id=user2.id)])

turkeylovers = Recipe(title='turkeywinsgs', link = 'madeuplink.com',savedrecipes=[FavoriteRecipe(user_id=user1.id),
FavoriteRecipe(user_id=user2.id)])

fruitlovers = Recipe(title='fruitrecipes', link = 'madeupfruitlink.org',savedrecipes=[FavoriteRecipe(user_id=user1.id),
FavoriteRecipe(user_id=user2.id), FavoriteRecipe(user_id=user3.id)])



db.session.add_all([veggielovers, turkeylovers, fruitlovers])
db.session.commit()