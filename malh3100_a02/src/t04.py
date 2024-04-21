"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Aikem Malhotra
ID:      169053100
Email:   malh3100@mylaurier.ca
__updated__ = "2024-01-19"
-------------------------------------------------------
"""
from Food_utilities import food_table
from Food import Food
def main():
    food = Food("BBQ Pork",1,False,920)
    food1 = Food("Beef with Green Pepper",1,False,251)
    foods = [food1,food]
    food_table(foods)
main()