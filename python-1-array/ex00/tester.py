#!/usr/bin/env python3.10
from give_bmi import give_bmi, apply_limit
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

def main():
    """
    Main function for testing purposes.
    """
    try:
        height = [2.71, 1.15]
        weight = [165.3, 38.4]
        # height = [(23,31, [[],[None]]), 2]
        # height = [(None), [], -31,3, -0]
        # weight = [(None), (), 1, 34,44444444444444444444444444444444444444444444444]
        bmi = give_bmi(height, weight)

        print(bmi, type(bmi))
        print(apply_limit(bmi, 26))
    except TypeError as te:
        print_error(TypeError, str(te))
    except ValueError as ve:
        print_error(ValueError, str(ve))
    except Exception as e:
        print_error(Exception, str(e))
        # print(f"Error: {e}")

if __name__ == "__main__":
    main()

# Expected output:
# $> python tester.py
# [22.507863455018317, 29.0359168241966] <class'list'>
# [False, True]
# $>