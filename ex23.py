##Reverse the input statments.


str=input('Enter a sentence:\n')
#method 1

str2 = str.split()
print(' '.join(str2[::-1]))

#method 2
str2=reversed(str2)
print(' '.join(str2))



