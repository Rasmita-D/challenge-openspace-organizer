import random

foo = ['a', 'b', 'c', 'd', 'e']
print(random.choice(foo))

names_too=foo.copy()
for i in range(len(foo)):
   table=random.choice(foo)
