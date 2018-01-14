# Encapsulation
# Import module and using its
from ex26 import Circle, Rectangle

# Provided radius value
c = Circle()
c.setRadius()
radii = c.getRadius()
area = c.area()
print('Radius is ', radii)
print('Area of a circle with radius {}, is {}'.format(radii, area))

# Default radius

c = Circle()
c.setRadius()
radii = c.getRadius()
area = c.area()
print('Radius is ', radii)
print('Area of a circle with radius {}, is {}'.format(radii, area))

# Provided length and breadth values
r = Rectangle()
r.setlenbredth(5, 10)
print(r.getlenbreadth())
print(r.area())

# default length=1 and breadth=1
r = Rectangle()
r.setlenbredth()
print(r.getlenbreadth())
print(r.area())


def long_function_name(var_four,
                       va2, va4):

    print(va2+var_four+va4)
long_function_name(25,13,15)
str='hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh'
