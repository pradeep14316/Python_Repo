#dictionaries
dict={}
print(type(dict))

dict1={"Mark":23,"Johnson":22,"China":25,"Indiana":21}
dict2={"Name":'shyam',"Id":2705,"DOB":10051989,"Location":'India'}
#update dictionaries
dict["pradeep"]=20
print(dict)

#accessing values in dictionaries
print(dict1['Indiana'])

#deleting dictionary elements

del dict1['Johnson']   #delete given dictionary element
print(dict1)

dict1.clear()         # clear all the  entries in dictionary
print(dict1)

del dict1     # delete the dictionary completely
#print(dict1)


print(dict2.keys())
print(dict2.values())
print(dict2.items())
print(dict2.get('Name'))


print(str(dict2))