from datetime import datetime

# To write to an existing file, you must add a parameter to the open() function:
# "a" - Append - will append to the end of the file
# "w" - Write - will overwrite any existing content
# If 'demofile2.txt' is doesn't exist it will be created automatically.

# Write to an Existing File
f = open("demofile2.txt", "a")
f.write("Now the file has more content!\n")
f.close()
f = open("demofile2.txt", 'r')
print(f"{f.name};")
print(f.read().strip())
print("1-------------")

# Note: the "w" method will overwrite the entire file.
f = open("demofile3.txt", 'w')
f.write("Opps! I have deleted the content! DAMNN")
f.close()
f = open("demofile3.txt", 'r')
print(f"{f.name};")
print(f.read().strip())
print("2-------------")

# Create a New File
# To create a new file in Python, use the open() method, with one of the following parameters:
# "x" - Create - will create a file, returns an error if the file exists
# "a" - Append - will create a file if the specified file does not exists
# "w" - Write - will create a file if the specified file does not exists
try:
	f = open("myfile.txt", 'x') # If file already have must be throw FileExistsError.
	print("File created successfully!")
	f.write("You can write to file.\n")
	f.close()
except FileExistsError:
	print("EXCEPTION: FileExistError: File already exist!")
print("3-------------")

# 'a' do not throw any exception
# Appends to the end of the file or creates a new file if it doesn't exist.
# Also doesn't throw an error.
try:
	with open("myfile.txt", 'a') as f: # We are using 'with', not need to use f.close().
		f.write("This line was writen to the file in 'a' mode.\n")
	print("Line added to file in 'a' mode!")
	with open("myfile.txt", 'r') as f:
		print(f"{f.name};")
		print(f.read().strip())
except Exception as e:
	print(f"ERROR: EXCEPTION: {e}")
print("4-------------")

# 'w' do not throw any exception
# Creates a file or overwrites an existing file.
# Also doesn't throw an error.
try:
	with open("myfile.txt", 'w') as f:
		current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		f.write(f"This line was writen to the file in 'w' mode. - {current_time}\n")
	print("Writed to file in 'w' mode!")
	with open("myfile.txt", 'r') as f:
		print(f"{f.name};")
		print(f.read().strip())
except Exception as e:
	print(f"ERROR: EXCEPTION: {e}")
print("5-------------")
