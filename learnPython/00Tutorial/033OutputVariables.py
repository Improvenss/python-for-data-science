# Output Variables
x = "yuandre"
print(x) # yuandre
print("1-------------")

x = "yuandre"
y = "hello"
z = "ball"
print(x, y, z) # yuandre hello ball
print("2-------------")


x = "Toyota"
y = "Nissan"
z = "Audi"
print(x + y + z) # ToyotaNissanAudi
print("3-------------")

# For numbers, the + character works as a mathematical operator:
x = 5
y = 10
print(x + y) # 15
print("4-------------")

# In the print() function, when you try to combine a string and a number
#  with the + operator, Python will give you an error:
try:
	x = 5
	y = "yuandre"
	print(x + y) # ERROR
except Exception as e:
	print(f"ERROR: EXCEPTION: {e}")
print("5-------------")

# The best way to output multiple variables in the print() function is to
#  separate them with commas, which even support different data types:
x = 5
y = "yuandre"
print(x, y)
print("6-------------")