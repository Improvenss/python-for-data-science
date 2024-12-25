# Built-in Data Types
# Text Type:		str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:		dict
# Set Types:		set, frozenset
# Boolean Type:		bool
# Binary Types:		bytes, bytearray, memoryview
# None Type:		NoneType

# Getting the Data Type
# You can get the data type of any object by using the type() function:
x = 5
print(f"Type of variable x -> ({type(x)})")

# Setting the Data Type
# In Python, the data type is set when you assign a value to a variable:
x = "Hello World"							 # str
x = 20										 # int
x = 20.5									 # float
# Karmaşık sayılar. Gerçek ve sanal kısmı içerir.
# Complex numbers. Includes real and imaginary parts.
x = 1j										 # complex
# Sıralı ve değiştirilebilir veri yapısı. Elemanlar farklı türde olabilir.
# Sequential and mutable data structure. Elements can be of different types.
x = ["apple", "banana", "cherry"]			 # list
# Sıralı ancak değiştirilemez veri yapısı.
# An ordered but immutable data structure.
x = ("apple", "banana", "cherry")			 # tuple
# Belirli bir aralığı temsil eder. Genellikle döngülerde kullanılır.
# Represents a specific range. Often used in loops.
x = range(6)								 # range -> 0 to 5 -> 0,1,2,3,4,5
# Anahtar-değer çiftlerinden oluşur.
# It consists of key-value pairs.
x = {"name" : "John", "age" : 36}			 # dict (Dictionary)
# Sırasız, eşsiz elemanlar kümesi.
# An unordered, unique set of elements.
x = {"apple", "banana", "cherry"}			 # set
# Değiştirilemez set.
# Unchangeable set.
x = frozenset({"apple", "banana", "cherry"}) # frozenset
x = True									 # bool
# Bayt veri tipi, bir dizi byte içerir.
# The byte data type contains a sequence of bytes.
x = b"Hello"								 # bytes
# Bayt dizisinin değiştirilebilir versiyonu.
# A mutable version of the byte array.
x = bytearray(5)							 # bytearray
# Bir veri yapısının belleğine doğrudan erişim sağlar.
# Provides direct access to the memory of a data structure.
x = memoryview(bytes(5))					 # memoryview
x = None									 # NoneType

# Setting the Specific Data Type
# If you want to specify the data type, you can use the following constructor functions:
x = str("Hello World")						 # str
x = int(20)									 # int
x = float(20.5)								 # float
x = complex(1j)								 # complex
x = list(("apple", "banana", "cherry"))		 # list
x = tuple(("apple", "banana", "cherry"))	 # tuple (demet demek)
x = range(6)								 # range
x = dict(name = "John", age = 36)			 # dict
x = set(("apple", "banana", "cherry"))		 # set
x = frozenset(("apple", "banana", "cherry")) # frozenset
x = bool(True)								 # bool
x = bytes("Hello")							 # bytes
x = bytearray(5)							 # bytearray
x = memoryview(bytes(5))					 # memoryview