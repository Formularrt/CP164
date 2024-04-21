"""
-------------------------------------------------------
[assignment 4, task 2]
-------------------------------------------------------
Author:  Aikam Malhotra
ID:         169053100
Email:   malh3100@mylaurier.ca
__updated__ = "2024-02-02"
-------------------------------------------------------
"""
from Queue_array import Queue

s1 = Queue()
s2 = Queue()
s2.insert(1)
s1.insert(10)

equals = s1 == s2

print(equals)