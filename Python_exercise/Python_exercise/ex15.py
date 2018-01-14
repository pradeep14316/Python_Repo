#Write a program that asks the user how many Fibonnaci numbers to generate and then generates them
def get_integer():
    num=int(input("Enter how many Fibonnaci numbers to generate:\n"))
    return num
def fibonacci():
    x=0
    y=1
    num=get_integer()
    print("0\n1")
    for seq in range(1,num-1):
        y,x=y+x,y
        print(y)

fibonacci()