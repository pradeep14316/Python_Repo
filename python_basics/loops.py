#for loop iterating using  range()
"""for i in range(1,10):
    print("current loop is:{0}".format(i) )
"""
#Iterating  over list using for loop
Names=['Maria','suparna','anantha','sanam','vignesh','bala','ayyapa']
"""count=0

print("Student Enrolled in our school are:")
for names in Names:
    count+=1
    print("{0}.{1}".format(count,names))
"""

#iterating using list by while loop
"""i=0
while True:
    print(Names[i])
    i+=1
    if Names[i]=='ayyapa':
        print(Names[i])
        break
print("while loop is terminated")
"""
#using for loop iterating a string
f=[]
f_name="Adam Gilbert"
list=f_name.split(' ')
print(list)
for i in list:
    f.append(i)
print(f)
