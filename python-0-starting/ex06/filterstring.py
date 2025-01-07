#!/usr/bin/env python3.10
import sys as sys
from ft_filter import ft_filter as ft_filter


def print_error(exception: Exception, message: any) -> int:
    """
    Prints an error message to standard error and exits the program.

    Args:
    exception (Exception): The exception class related to the error.
    message (any): The error message to display.

    Returns:
    int: This function does not return; it terminates the program.

    Side Effects:
    - Prints the error message to stderr.
    - Exits the program with a non-zero status code.
    """
    print(f"{exception.__name__}: {message}", file=sys.stderr)
    exit()


def validate_arguments(args: any):
    """
    Validates the command-line arguments.

    Args:
        args (list): The list of arguments passed to the program.

    Raises:
        AssertionError: If the number of arguments is not 2 or if the \
arguments are of incorrect types.
    """
    if len(args) != 2 or not args[1].isdigit():
        raise AssertionError("the arguments are bad")


def main():
    """
    Main function to filter words from the input string based on length.

    The program expects two arguments: a string and an integer.
    Outputs a list of words from the string with a length greater than \
the given integer.
    """
    try:
        # Validate arguments
        validate_arguments(sys.argv[1:])

        # Parse arguments
        input_string = sys.argv[1]
        min_length = int(sys.argv[2])

        # Split the input string into words
        words = input_string.split()

        # Use a lambda and ft_filter to filter words by length
        filtered_words = ft_filter(lambda word: len(word) > min_length, words)

        # Convert the result to a list and print
        result = [word for word in filtered_words]
        print(result)
    except AssertionError as ae:
        print_error(AssertionError, str(ae))
    except Exception as e:
        print_error(Exception, str(e))


if __name__ == "__main__":
    main()
