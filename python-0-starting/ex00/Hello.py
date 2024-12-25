ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

# ---------------
ft_list[1] = "World!"
# ft_list.pop()
# ft_list.append("World!")
# ---------------
ft_tuple = (ft_tuple[0], "Turkiye!")
# ---------------
ft_set = {"Hello", "Kocaeli!"}
# ft_set.pop()
# ft_set.add("Kocaeli")
# ---------------
ft_dict["Hello"] = "42Kocaeli!"
# ---------------

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)

"""
Expected output:
$>python Hello.py | cat -e
['Hello','World!']$
('Hello','France!')$
{'Hello','Paris!'}$
{'Hello': '42Paris!'}$
$>
"""