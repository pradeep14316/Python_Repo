
students=[]

class Test():
    def __init__(self,name,id ='225'):
        self.name = name
        self.id = id
        students.append(self)

    def __str__(self):
        return "Student "+self.name.capitalize() +"\nId: "+self.id



clark=Test("clark")
print(clark)