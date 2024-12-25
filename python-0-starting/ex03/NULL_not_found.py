# Allowed functions: None
def NULL_not_found(object: any) -> int:
	object_type = type(object)
	
	# Output formatting
	if object is None:
		print(f"Nothing: {object} {object_type}")
	elif isinstance(object, float) and object != object:  # NaN control
		print(f"Cheese: {object} {object_type}")
	elif object_type is int:
		print(f"Zero: {object} {object_type}")
	elif object_type is str and object == '':
		# print(f"Empty: {object} {object_type}")
		print("Empty:", object_type)
	elif object_type is bool and object is False:
		print(f"Fake: {object} {object_type}")
	else:
		print("Type not Found")
		return (1)
	return (0)

"""
Expected output:
$>python NULL_not_found.py | cat -e
$>
"""