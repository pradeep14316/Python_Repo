
#File Operations

##Write Mode


def write_file():
    f=open('file.txt','w')
    f.write('Welcome to Python Basics')
    f.close()
print("Successfully written to the file 'file.txt'")

##Read Mode

def read_file():
    f=open('file.txt','r')
    for i in f.readlines():
        print(i)
    f.close()
print("Read the content from file 'file.txt'")

##Append Mode

def append_file():
    f=open('file.txt','a')
    f.write("""\n This is the second line of the text file.\n In Append mode files are wriiten in a continous form.The text will be concat with the previous statements""")
    f.close()
print("Successfully written to the file 'file.txt'")

write_file()

read_file()

append_file()

read_file()








