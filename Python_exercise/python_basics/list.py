#Lists
"""
list1=[]
print("list1")
list1.append('Mathews')
print(list1)
list2=['alpha','beta','gama','nuclear','etc']
print(list2)

#Access a particular element using index[0,1..]

print(list1[0])
#returns an error

#print(list1[2])
#to know the length of a list use len()
print(len(list2))

#we can also use splicing method to select a particular values in a list[0:..]or [-1:]#

#  print 0,1 values
print(list2[0:2])

#print all the values
print(list1[0:])

# print the  last value
print(list1[-1:])

#print 1,2,3,4 values
print(list2[1:5])

"""
# list operations
#clear(list),del,remove(vallue),insert(index,value),pop()
list3=[1,2,3,4,5,6,7,8,9,10]

print("Before clear opearation:\nlist3=",list3,"\n")
list3.clear()
print("After clear operation:\nlist3=",list3,"\n")

list2=['alpha','beta','gama','nuclear','etc']
list3=[1,2,3,4,5,6,7,8,9,10]


print("Before insert opearation:\nlist2=",list2,"\n")
list2.insert(3,2)
print("After insert operation:\nlist2=",list2,"\n")


print("Before pop opearation:\nlist3=",list3,"\n")
list3.pop()
print("After pop operation:\nlist3=",list3,"\n")

print("Before remove opearation:\nlist3=",list3,"\n")
list3.remove(5)
print("After remove operation:\nlist3=",list3,"\n")
del list3
print("list3 has suuccessfully deleted!!")