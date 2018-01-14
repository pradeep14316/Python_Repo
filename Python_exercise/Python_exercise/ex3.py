def divisors():
    divisors_list=[]
    dividend=int(input("Enter a Number:\n"))
    for divisor in range(2,dividend+1):
        if dividend % divisor == 0:
            divisors_list.append(divisor)
    print("List of divisors of the given dividend '{0}':{1} ".format(dividend,divisors_list))
divisors()