# Many Values to Multiple Variables
#  Python allows you to assign values to multiple variables in one line:
x, y, z = "Hello", "yuandre", "welcome."
print(x, y, z)

# One Value to Multiple Variables
#  And you can assign the same value to multiple variables in one line:
x = y = z = "yuandre"
print(x, y, z)

# Unpack a Collection (Tuple)
#  Tuples are used to store multiple items in a single variable.
#  Tuple is one of 4 built-in data types in Python used to store
#  collections of data, the other 3 are List, Set, and Dictionary,
#  all with different qualities and usage. A tuple is a collection
#  which is ordered and unchangeable.
# If you have a collection of values in a list, tuple etc.
#  Python allows you to extract the values into variables.
#  This is called unpacking.
cars = ["Toyota", "Nissan", "Audi"]
x, y, z = cars
print(x, y, z)