# define the Vehicle class
class Vehicle:
    name = "Tesla"
    kind = "car"
    color = "Red"
    value = 120000.00
    def description(self):
        desc_str = "My %s  %s %s worth $%.2f." % (self.color, self.name, self.kind, self.value)
        return desc_str
# your code goes here
car1=Vehicle()

# test code

print(car1.description())
