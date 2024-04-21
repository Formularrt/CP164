"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Aikem Malhotra
ID:      169053100
Email:   malh3100@mylaurier.ca
__updated__ = "2024-01-26"
-------------------------------------------------------
"""
from utilities import array_to_stack
from Stack_array import Stack

source1 = Stack()
array_to_stack(source1, [3, 6, 1, 7, 9, 14])
print(source1._values)
source1.reverse()

print(source1._values)

