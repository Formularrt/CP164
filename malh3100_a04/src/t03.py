"""
-------------------------------------------------------
[assignment 4, task 3]
-------------------------------------------------------
Author:  Aikam Malhotra
ID:         169053100
Email:   malh3100@mylaurier.ca
__updated__ = "2024-02-02"
-------------------------------------------------------
"""
from Queue_array import Queue
from functions import queue_split_alt

source = Queue()
source.insert(1)
source.insert(2)
source.insert(3)
source.insert(4)
source.insert(5)
print(source._values)
target1, target2 = queue_split_alt(source)

print(target1._values, target2._values)