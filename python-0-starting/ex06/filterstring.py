# from ft_filter import filter as filter


# def main():
#     print("hello world")
#     filter()
#     print("original filter function usage samples ->")


# # Allowed functions : sys or any other library that allows to receive the args
# if __name__ == "__main__":
#     main()

def ft_filter(function, iterable):
    """
    Custom implementation of the filter function.

    Args:
    function (callable or None): A function to test each item or None.
    iterable (iterable): The iterable whose items will be filtered.

    Returns:
    generator: A generator yielding items for which function(item) is True.
    """
    if function is None:
        return (item for item in iterable if item)
    return (item for item in iterable if function(item))


def is_even(num):
    """
    Check if a number is even.

    Args:
    num (int): The number to check.

    Returns:
    bool: True if the number is even, False otherwise.
    """
    return num % 2 == 0


def main():
    """
    Main function to test ft_filter and handle any errors.
    """
    try:
        numbers = [1, 2, 3, 4, 5, 6, 0]
        filtered_numbers = ft_filter(is_even, numbers)
        print(list(filtered_numbers))

        truthy_values = ft_filter(None, [0, 1, False, True, "hello", ""])
        print(list(truthy_values))

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()