"""
-------------------------------------------------------
[assignment 4, task 4]
-------------------------------------------------------
Author:  Aikam Malhotra
ID:         169053100
Email:   malh3100@mylaurier.ca
__updated__ = "2024-02-02"
-------------------------------------------------------
"""
from Queue_array import Queue

q = Queue()

q.insert(1)
q.insert(2)
q.insert(3)
q.insert(4)
q.insert(5)

target1, target2 = q.split_alt()

print("Target1: {}".format(target1._values))
print("Target2: {}".format(target2._values))