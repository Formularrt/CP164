"""
-------------------------------------------------------
[assignment 4, task 6]
-------------------------------------------------------
Author:  Aikam Malhotra
ID:         169053100
Email:   malh3100@mylaurier.ca
__updated__ = "2024-02-02"
-------------------------------------------------------
"""
from Priority_Queue_array import Priority_Queue

pq = Priority_Queue()
pq.insert(1)
pq.insert(2)
pq.insert(3)
pq.insert(4)
pq.insert(5)

key = 3

print(pq._values)
target1, target2 = pq.split_key(key)
print(target1._values, target2._values)