#From given lists take the common elements and append to a new list. No duplicates

randa = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
randb = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


#remove duplicates from lists

rand_a = set(randa)
rand_b = set(randb)



#compare the two lists

match = []
for check1 in rand_a:
    if (check1 in rand_b):
        match.append(check1)
print (set(match))