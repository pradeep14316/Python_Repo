"""Regular Expressions
^       start
$       stop
.       Any character
*       Match one character
+       Match one charcter
?       Non-greedy
\s      Whitespace
\S      Non-Whitespace
[abc]   Match one character ranges a-c
[^abc]  Match one charcter ranges d-z


"""


import re

str="Hi this is praadeep "\
    "1.Welcome to python programming" \
    "2.lets discuss about some regular expressions "\
    "3.In 1994 python was inentedpradeep.vangala1@gmail.com by @_ netherlan linus torvalds"\
    "4. age is 25yrs and dob    is 27 may 1993 cloudguy@gmail.com    "

matchobj=re.findall('\S+@\S+',str)
match=re.findall('[\w]+',str)
print(match)
print(matchobj)