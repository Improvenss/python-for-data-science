# open() function;
# The key function for working with files in Python is the open() function.
# The open() function takes two parameters; filename, and mode.
# 	"r" - Read - Default value. Opens a file for reading, error if the file does not exist
# 	"a" - Append - Opens a file for appending, creates the file if it does not exist
# 	"w" - Write - Opens a file for writing, creates the file if it does not exist
# 	"x" - Create - Creates the specified file, returns an error if the file exists
# In addition you can specify if the file should be handled as binary or text mode
# 	"t" - Text - Default value. Text mode
# 	"b" - Binary - Binary mode (e.g. images)

# f = open("demofile.txt")
# f = open("demofile.txt", "rt")
# Because "r" for read, and "t" for text are the default values, you do not need to specify them.

# Open file.
f = open("demofile.txt", "rt")
print(f.read(), '\n') # This .read() function returns full readed data.

# Open with full path.
f = open("/Users/yuandre/Desktop/python-for-data-science/learnPython/01FileHandling/demofile.txt", "rt")
print(f.read(5), '\n') # But you can read only 5 character. (Hello)

f.close() # Closing file description.