# Allowed functions : sys or any other library that allows to receive the args
import sys as sys

# print(sys.argv) # How to get arguments in python?

argc = len(sys.argv) - 1
# print("argc->", argc)
if (argc == 0 or argc >= 2):
	if (argc >= 2):
		print("AssertionError: more than one argument is provided")
	exit()
try:
	integer_argv = int(sys.argv[1]) # If argument is not integer; throw except.
	if (integer_argv % 2 == 0):
		print("I'm Even.")
	else:
		print("I'm Odd.")
except ValueError:
	print("AssertionError: argument is not an integer")
except Exception as e:
	print(f"ERROR: {e}")