# Global Variables
# Variables that are created outside of a function
#  (as in all of the examples in the previous pages)
#  are known as global variables.
# Global variables can be used by everyone, both inside
#  of functions and outside.
x = "yuandre"

def	myFunc():
	print("Hello, I am " + x)
	print(f"Hello, I am {x}")
myFunc()
print("1-----------")

# If you create a variable with the same name inside a function,
#  this variable will be local, and can only be used inside the function.
#  The global variable with the same name will remain as it was,
#  global and with the original value.
y = "Wall-E"

def	movies():
	y = "Cars"
	print(y)
movies()
print(y)
print("2-----------")

# The global Keyword
# Normally, when you create a variable inside a function,
#  that variable is local, and can only be used inside that function.
# To create a global variable inside a function, you can use
#  the global keyword.
try:
	def	funcGlobal():
		global	g
		g = "bird"
	print(f"Before the global Keyword ({g})") # ERROR
except Exception as e:
	print(f"ERROR: EXCEPTION: {e}")
funcGlobal()
print(f"After the global Keyword ({g})")
print("3-----------")

# Also, use the global keyword if you want to change a
#  global variable inside a function.
z = "Damnnnnnnn"

def	changeGlobal():
	global	z
	z = "ehehehehe"
print(f"Before the global change function ({z})")
changeGlobal()
print(f"After the global change function ({z})")
print("4-----------")