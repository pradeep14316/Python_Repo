#Generate Password

import random

#method 1
def pass_gen():
    while True:
        user = input('Welcome to password generator.To Generate password press "y" or "n" to exit:\n')

        if user=='y':
            str1 = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
            str2 = random.sample('abcdefghijklmnopqrstuvwxyz', 3)
            str3 = ''.join(str2)
            num = random.randrange(101, 999)
            symbol1 = random.choice('~!@#$%^&*()')
            symbol2 = random.choice('~!@#$%^&*()')
            symbol3 = random.choice('~!@#$%^&*()')

            passwd=str1+symbol3+str3+symbol1+str(num)+symbol2
            print("Your generated password is {0}".format(passwd))
        else:
            break

#method 2
def passgen():
    s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
    paswd_length = 10
    p =  "".join(random.sample(s,paswd_length ))
    print (p)

pass_gen()
print('method2')
passgen()