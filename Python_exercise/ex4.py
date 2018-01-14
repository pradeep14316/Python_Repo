#write a program that returns a list that contains only the elements that are common between the lists (without duplicates).
# Make sure your program works on two lists of different sizes.

import random

#compute random lists
randa = []
randb = []

for a in range(0,40):
    a = random.randint(0,40)
    randa.append(a)
for b in range(0,45):
    b = random.randint(0,30)
    randb.append(b)

#remove duplicates on the random lists
rand_a = set(randa)
rand_b = set(randb)

#compare the two random lists
match = []
for check1 in rand_a:
    if (check1 in rand_b):
        match.append(check1)
print (set(match))