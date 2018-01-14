#type hinting
#Integers
def add(a:int,b:int):
    return a+b
print(add(5,6))

a=5
b=2

#strings
var="Hello World"
var1='Hello World'
var2="""Hello World"""
print(var,var1,var2)

print(var.split())
print('hello '.isdigit())
print('123'.isdigit())
print(''.isalpha())
print('hello'.isalpha())
print("bigger" if a>b else "smaller")