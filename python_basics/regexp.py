""""".	dot matches any character except newline
\w	matches any word character i.e letters, alphanumeric, digits and underscore ( _ )
\W	matches non word characters
\d	matches a single digit
\D	matches a single character that is not a digit
\s	matches any white-spaces character like \n, \t, spaces
\S	matches single non white space character
[abc]	matches single character in the set i.e either match a, b or c
[^abc]	match a single character other than a, b and c
[a-z]	match a single character in the range a to z.
[a-zA-Z]	match a single character in the range a-z or A-Z
[0-9]	match a single character in the range 0-9
^	match start at beginning of the string
$	match start at end of the string
+	matches one or more of the preceding character (greedy match).
*	matches zero or more of the preceding character (greedy match).
"""
import re
str="Hi welcome to python programming" \
    "Today is most auspicious day in my life i am able to write python programming on my own." \
    "so let's start"\
    "Todays topic is regular expressions. I think you have an idea on regexp which is used to search data from a large data files. if you  have any doubt email me on pradeepred1@outlook.com" \
    "and my i have another email id that is vangalapradeep123@gmail.com, so you can chat me on hangouts. m hangouts id is pradeep.vangala1@gmail.com"

#lets search the email id's i have provided in the sample text

match=re.search("H*",str)
if match:
    print(match.group())