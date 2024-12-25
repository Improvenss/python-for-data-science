import sys as sys


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


def print_analyse_input(input: str, input_len: int):
    """
    Analyzes the given text and prints statistical information about it.

    Args:
    input (str): The text to analyze.
    input_len (int): The length of the text.

    Prints:
    - Total number of characters in the text.
    - Count of uppercase letters.
    - Count of lowercase letters.
    - Count of punctuation marks.
    - Count of spaces.
    - Count of digits.
    """
    upper_count = sum(c.isupper() for c in input)
    lower_count = sum(c.islower() for c in input)
    punctuation_count = sum(c in ".,!?;:'\"-()[]{}<>@#$%^&*" for c in input)
    space_count = sum(c.isspace() for c in input)
    digit_count = sum(c.isdigit() for c in input)

    print(f"The text contains {input_len} characters:")
    print(f"{upper_count} upper letters")
    print(f"{lower_count} lower letters")
    print(f"{punctuation_count} punctuation marks")
    print(f"{space_count} spaces")
    print(f"{digit_count} digits")


def check_arguments(argv_len: int) -> int:
    """
    Validates the number of command-line arguments.

    Args:
    argv_len (int): The number of command-line arguments.

    Returns:
    int:
    - 1 if exactly one argument is provided.
    - Exits the program with an error if no argument or more than one \
        argument is provided.

    Raises:
    IndexError: If no arguments are provided.
    AssertionError: If more than one argument is provided.
    """
    # If no argument entered
    if (argv_len == 1):
        raise IndexError("no argument provided")
    # 1 argument
    if (argv_len == 2):
        return 1
    # 1+ argument
    if (argv_len > 2):
        raise AssertionError("more than one argument is provided")
    return 0


def main():
    """
    Entry point of the program. Manages user input, handles exceptions,
    and calls the analysis function.

    Workflow:
    - Validates the number of command-line arguments using `check_arguments`.
    - Prompts the user for input if no arguments are provided.
    - Calls `print_analyse_input` to analyze the text and display results.
    - Handles exceptions such as IndexError and AssertionError using \
        `print_error`.
    """
    user_input = str()

    try:
        if (check_arguments(len(sys.argv)) == 1):
            user_input = sys.argv[1]
    except IndexError:
        user_input = input("What is the text to count?\n")
    except AssertionError as e:
        print_error(AssertionError, str(e))
    except Exception as e:
        print_error(Exception, str(e))
    print_analyse_input(user_input, len(user_input))


"""
You can run this command to test it;
python3.10 building.py "Python 3.0, released in 2008, was a major revision \
that is not completely backward-compatible with earlier versions. Python 2 \
was discontinued with version 2.7.18 in 2020."
"""
"""
Expected outputs:
$>python building.py "Python 3.0, released in 2008, was a major revision that\
is not completely backward compatible with earlier versions. Python 2 was\
discontinued with version 2.7.18 in 2020."
The text contains 171 characters:
2 upper letters
121 lower letters
8 punctuation marks
25 spaces
15 digits
$>
"""
# Allowed functions : sys or any other library that allows to receive the args
# LINK: https://www.geeksforgeeks.org/python-docstrings/
if __name__ == "__main__":
    main()
