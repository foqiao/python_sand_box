from collections import namedtuple

#nametuple constructor
Color = namedtuple('color', ['red', 'green', 'blue'])
#color based on Color object constructor
color = Color(55, 155, 255)

#print out the argument represents red
print(color.red)