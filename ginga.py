import re

text="Bounce Hi welcome to Bounce the World yo gonna rock it here "
regex=
result=re.search('^[BW].+\w ', text)
print(result.group())
