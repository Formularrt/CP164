
from List_linked import List

l = List()
l.append(1)
l.append(2)
l.append(3)
l.append(4)
l.append(5)

even, odd = l.split_alt()
print(even._front._next._value, odd._front._next._value)