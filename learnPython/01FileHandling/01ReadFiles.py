# The open() function returns a file object, which has a read() method for reading the content of the file:

# Read Only Parts of the File
# By default the read() method returns the whole text, but you can also specify how many characters you want to return:
f = open("demofile.txt", "r")
print(f.read()) # This .read() function returns full readed data.
print("1-------------")

f = open("demofile.txt", "r")
print(f.read(5)) # But you can read only 5 character. (Hello)
print("2-------------")

# Read lines
f = open("demofile.txt", "r")
print(f.readline()) # output -> (Hello! Welcome to demofile.txt)
print("3-------------")

f = open("/Users/yuandre/Desktop/python-for-data-science/learnPython/01FileHandling/demofile.txt", "r")
print(f.readline(4)) # You can read only 4 character from readed line. output-> (Hell)
print("4-------------")

num = 0
f = open("demofile.txt", "r")
for x in f:
	num += 1
	print(num, x)
print("5-------------")
# or

# Python with Context Manager -> 'with'
# You doesn't need to close file, because 'with' closing automatically.
num = 0
with open("demofile.txt", "r") as f:
	for x in f:
		num += 1
		print(f"{num}-{x.strip()}") # Also you can remove stripes with .strip() func. f-string f"{}"
print("6-------------")

f.close()