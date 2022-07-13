# creates a tuple defined as an (x and y) axis.
point = (2.0, 3.0) 
# creates a 3-dimensional axis by adding to the original tuple.
point_3d = point + (4.0,) 
print(point_3d) # prints the tuple "point_3d".
x, y, z = point_3d # unpacks the tuple "point_3d" into three new items according to their place in the axis
print(x) # prints item from "point_3d" x-axis point.
print(y) # prints item from "point_3d" y-axis point.
print(z) # prints item from "point_3d" z-axis point.

# prints the statement and unpacked tuple using the substitution characters "%s".
print("My name is: %s %s" % ("Melissa", "Gibson")) 
person = ('Melissa Gibson', 31, '444-444-4444') # assigns items to "person".
person2 = ('Dumbledore', 115, '') # assigns items to "person2" while leaving the third item blank.
print(person[0]) # prints the first item (name) in the tuple "person".
print(person2[1]) # prints the second item (age) in the tuple "person2".

