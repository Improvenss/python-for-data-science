import os as os

# List of files to be deleted
files = ["demofile2.txt", "demofile3.txt", "myfile.txt"]

# *****************************************************************************
# Try to delete files
# Clearest/Best/Clean code.
for file in files:
	try:
		if os.path.exists(file):
			os.remove(file)
			print(f"{file} successfully deleted!")
		else:
			print(f"{file} doesn't exist!")
	except Exception as e:
		print(f"ERROR: EXCEPTION: {type(e).__name__}: {str(e)}")
print("1---------------")
# *****************************************************************************

# Delete a File
# To delete a file, you must import the OS module, and run its os.remove() function:
try:
	os.remove('demofile2.txt')
	os.remove('demofile3.txt')
	os.remove('myfile.txt')
except Exception as e:
	print(f"ERROR: EXCEPTION: {type(e).__name__}: {str(e)}") # {str(e)} or {e} both same.
print("2---------------")

# Check if File exist:
# To avoid getting an error, you might want to check if the file exists before you try to delete it:
try:
	if os.path.exists("demofile2.txt"):
		os.remove('demofile2.txt')
		print("demofile2.txt sucessfully deleted!")
	else:
		print("demofile2.txt doesn't exist!")
	if os.path.exists("demofile3.txt"):
		os.remove('demofile3.txt')
		print("demofile3.txt sucessfully deleted!")
	else:
		print("demofile3.txt doesn't exist!")
	if os.path.exists("myfile.txt"):
		os.remove('myfile.txt')
		print("myfile.txt sucessfully deleted!")
	else:
		print("myfile.txt doesn't exist!")
except Exception as e:
	print(f"ERROR: EXCEPTION: {type(e).__name__}: {str(e)}") # {str(e)} or {e} both same.
print("3---------------")

# Delete Folder
# To delete an entire folder, use the os.rmdir() method:
try:
	os.mkdir("myfolder")
	print("myfolder created!")
except Exception as e:
	print(f"ERROR: EXCEPTION: {type(e).__name__}: {str(e)}") # {str(e)} or {e} both same.
print("4---------------")

try:
	if (os.path.exists("myfolder")):
		os.rmdir("myfolder")
		print("myfolder sucessfully deleted!")
except Exception as e:
	print(f"ERROR: EXCEPTION: {type(e).__name__}: {str(e)}") # {str(e)} or {e} both same.
print("5---------------")