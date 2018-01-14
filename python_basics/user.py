import datetime


class User:
    def __init__(self, name, dob):
        self.name = name
        self.dob = dob
        full_name = name.split(" ")

        # extracting first name and last name
        print(dob)
        self.first_name = full_name[0]
        self.last_name = full_name[-1]

    def age(self):
        try:
            today = datetime.date(2017, 12, 8)
            yyyy= self.dob[0:4]
            mm = self.dob[4:6]
            dd = self.dob[6:8]
            user_dob = datetime.date(yyyy, mm, dd)
            age_in_days = (today - user_dob).days
            age_in_years = (age_in_days / 365)
            return int(age_in_years)
        except ImportError:
            print("There is something not yet found")
        except IOError:
            print("check your input")
        except TypeError as e:
            print("Check the error",e)
        else:
            print("write a different code")
        finally:
            print("This is finaly executed")

user = User('Mathews H Gilbert', 19891227)
print('First_Name:', user.first_name)
print('Last_Name:', user.last_name)
print('Age:',user.age())
