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
from Food import Food
from Food_utilities import average_calories
def main():
    food = Food("grape",3,True,2)
    food1 = Food("chicken",2,False,1)
    food2 = Food("sushi",3,True,12)
    foods = [food,food1,food2]
    avg = average_calories(foods)    
    print(avg)
main()