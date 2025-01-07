#!/usr/bin/env python3.10
# Allowed functions : sys or any other library that allows to receive the args
import sys as sys

NESTED_MORSE = {
    " ": "/",
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.",
    "G": "--.", "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
    "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.",
    "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
    "Y": "-.--", "Z": "--..", "0": "-----", "1": ".----", "2": "..---",
    "3": "...--", "4": "....-", "5": ".....", "6": "-....", "7": "--...",
    "8": "---..", "9": "----."
}


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


def validate_args(args):
    """
    Validate the arguments passed to the program.

    Args:
        args (list): List of arguments passed to the script.

    Raises:
        AssertionError: If the number of arguments is not 2 \
(script name + input string) or if the input contains \
invalid characters.
    """
    if len(args) != 2:
        raise AssertionError("the arguments are bad")

    for char in args[1]:
        if char.upper() not in NESTED_MORSE:
            raise AssertionError("the arguments are bad")
    # all(): If all items are true will be return True.
    # if not all(char.upper() in NESTED_MORSE for char in args[1]):
    #     raise AssertionError("the arguments are bad")


def encode_to_morse(input_string):
    """
    Encode the input string into Morse code.

    Args:
        input_string (str): The string to encode.

    Returns:
        str: The Morse code representation of the input string.
    """
    # morse_list = list()
    # for char in input_string:
    #     morse_code = NESTED_MORSE[char.upper()]
    #     morse_list.append(morse_code)
    # return " ".join(morse_list)
    return ' '.join(NESTED_MORSE[char.upper()] for char in input_string)


def main():
    """Main function to execute the script logic.
    """
    try:
        validate_args(sys.argv)
        # morse_code = encode_to_morse(sys.argv[1])
        # print(morse_code.strip())
        # Remove extra whitespaces and specified characters from the start/end.
        print(encode_to_morse(sys.argv[1]).strip())
    except AssertionError as ae:
        print_error(AssertionError, str(ae))
    except Exception as e:
        print_error(Exception, str(e))


if __name__ == "__main__":
    main()
