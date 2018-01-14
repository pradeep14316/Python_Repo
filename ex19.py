import re

text=open('sam.txt')
count=0
for line in text:
    line = line.rstrip()

    if re.search('^[A-Z].+handy$', line):
        print(line,'-match found:{0}'.format(count))