#find the sum of digits in the number 100!
def factor(num):
    n = 1
    for i in range(2, num+1):
        n = n * i
        addition=sum(int(i) for i in str(n))
    return "sum of ", n, "is ", addition
print(factor(100))