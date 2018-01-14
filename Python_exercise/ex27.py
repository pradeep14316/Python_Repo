#Inheritance


class Contacts():
    def __init__(self,name,mobile):
        self.name=name
        self.mobile=mobile


class email(Contacts):
    def __init__(self):
        super().__init__()

        
        self.email = mail
        return self.name, self.mobile, self.email