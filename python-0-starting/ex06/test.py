from ft_filter import ft_filter as ft_filter

# print(filter.__doc__)
# print("-----------------")
# print(ft_filter.__doc__)

numbers = [-2, -1, 0, 1, 2]

# Testing filter() with lambda func()
positive_numbers_lambda = filter(lambda n: n > 0, numbers)
# positive_numbers_lambda_exception = filter(lambda n: n > 0, None)
# positive_numbers_lambda_exception = filter(lambda n: n > 0, 42)
# positive_numbers_lambda = filter(42, numbers)
ft_positive_numbers_lambda = ft_filter(lambda n: n > 0, numbers)
# ft_positive_numbers_lambda_exception = ft_filter(lambda n: n > 0, None)
# ft_positive_numbers_lambda_exception = ft_filter(lambda n: n > 0, 42)
# ft_positive_numbers_lambda = ft_filter(42, numbers)

print("Positive numbers (lambda) ->", positive_numbers_lambda)
print("Positive numbers (lambda) ->", list(positive_numbers_lambda))
print("ft_ Positive numbers (lambda) ->", ft_positive_numbers_lambda)
print("ft_ Positive numbers (lambda) ->", list(ft_positive_numbers_lambda))
# print("Positive numbers (lambda) exception ->", list(ft_positive_numbers_lambda_exception))
print("1----------------")

# Testing filter() with user-defined func()
def is_positive(n):
    return (n > 0)
positive_numbers_function = filter(is_positive, numbers)
ft_positive_numbers_function = ft_filter(is_positive, numbers)

print("Positive numbers (user-defined) ->", positive_numbers_function)
print("Positive numbers (user-defined) ->", list(positive_numbers_function))
print("ft_ Positive numbers (user-defined) ->", ft_positive_numbers_function)
print("ft_ Positive numbers (user-defined) ->", list(ft_positive_numbers_function))
print("2----------------")


# Testing without func()
truthy_values = filter(None, numbers)
ft_truthy_values = ft_filter(None, numbers)
truthy_values_different = filter(None, [0, 1, False, True, "hello", ""])
ft_truthy_values_different = ft_filter(None, [0, 1, False, True, "hello", ""])

print("Truthy values (numbers) -> ", list(truthy_values))
print("Truthy values (different) -> ", list(truthy_values_different))
print("ft_ Truthy values (numbers) -> ", list(ft_truthy_values))
print("ft_ Truthy values (different) -> ", list(ft_truthy_values_different))
print("3----------------")
