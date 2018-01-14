import re

NameAge = '''Janice is 22 and Theon is 33 Gabriel is 44 and Joey is 21'''

ages = re.findall('\d{1,3}', NameAge)
names = re.findall('[A-Z][a-z]*', NameAge)

agedict = {}

x = 0

for name in names:
    agedict[name] = ages[x]
    x = +1
print(agedict)
