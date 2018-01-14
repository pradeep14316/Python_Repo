#Ask the user for a string and print out whether this string is a palindrome or not.
#  (A palindrome is a string that reads the same forwards and backwards.)


def palindrome(string):
    str = string.casefold()
    rev_str = reversed(str) #revesre of a string
    if list(str) == list(rev_str):
        return ('Yes, it is a palindrome')
    else:
        return ("No, it is not a palindrome")

print(palindrome('deleveled'))

""" method 2 """

def palindromee(string):

    str = string.casefold()
    rev_str = str[::-1]         #revesre of a string

    if list(str) == list(rev_str):
        return ("Yes, it is a palindrome")
    else:
        return ("No, it is not a palindrome")
print(palindromee('repaper'))