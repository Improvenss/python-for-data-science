x = 5
y = "yuandre"
print(f"{x}	->	type() = {type(x)}")
print(f"{y}	->	type() = {type(y)}")
print("1---------------")

# Variables do not need to be declared with any particular type,
#  and can even change type after they have been set.
x = 4
x = "yuandre"
print(f"{x}	->	type() = {type(x)}")
print("2---------------")

# Casting
# If you want to specify the data type of a variable, this can be
#  done with casting.
x = str(3)
print(f"{x}	->	type() = {type(x)}")
x = int(3)
print(f"{x}	->	type() = {type(x)}")
x = float(3)
print(f"{x}	->	type() = {type(x)}")
print("3---------------")

# Get the Type
# You can get the data type of a variable with the type() function.
x = 5
y = "yuandre"
print(f"{x}	->	type() = {type(x)}")
print(f"{y}	->	type() = {type(y)}")
print("4---------------")

# Single or Double Quotes?
x = 'yuandre'
y = "yuandre"
#  Both the same as. '' = ""
print(f"{x}	->	type() = {type(x)}")
print(f"{y}	->	type() = {type(y)}")
print("5---------------")

# Case-Sensitive
# Variable names are case-sensitive.
a = 5
A = 10
#  A will not overwrite a
print(a, A, (a + A))
print("6---------------")