#Find the sum of digits in 1000!(Factorial)

num = 1
for i in range(1, 1000):
    num = i * num
addition = sum([int(num1) for num1 in str(num) ])
print("The value of 100! is:",num)
print("Sum of digits in 1000! is ",addition)





