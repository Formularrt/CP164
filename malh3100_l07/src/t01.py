"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Aikam Malhotra
ID:      169053100
Email:   malh3100@mylaurier.ca
__updated__ = "2024-01-31"
-------------------------------------------------------
"""
# Imports
from List_linked import List

l = List()

l.append(1)
l.append(2)
l.append(2)
l.append(4)
l.append(5)
l.append(2)
key = 2
p, c, i = l._linear_search_r(key)
print(p._value, c._value, i)