import sys
import string


def parsing(argv: list[str]) -> str:
    """
    Parsing the input that the program receives
    an returns the argv[1] as a string
    """
    if len(argv) > 2:
        raise AssertionError("More than one argument provided")
    if len(argv) == 1:
        return input("What is the text to count?\n")
    return argv[1]


def analyse_string(str: str) -> dict[str, int]:
    """
    Analysing the string received and returns an
    dictionary with the sums of the upper-case characters,
    lower-case characters, punctuation characters, digits, and spaces.
    """
    counter_dict = {
        "upper_case": 0,
        "lower_case": 0,
        "punctuation": 0,
        "spaces": 0,
        "digits": 0
    }

    for char in str:
        if char.isupper():
            counter_dict["upper_case"] += 1
        elif char.islower():
            counter_dict["lower_case"] += 1
        elif char in string.punctuation:
            counter_dict["punctuation"] += 1
        elif char.isspace():
            counter_dict["spaces"] += 1
        elif char.isdigit():
            counter_dict["digits"] += 1

    return counter_dict


def print_result(dictionary: dict[str, int]) -> None:
    """
    Prints the output of the analisation done
    """
    total_characters = sum(dictionary.values())

    print(f"The text contains {total_characters} characters:")
    print(f"{dictionary['upper_case']} upper letters")
    print(f"{dictionary['lower_case']} lower letters")
    print(f"{dictionary['punctuation']} punctuation marks")
    print(f"{dictionary['spaces']} spaces")
    print(f"{dictionary['digits']} digits")


def main() -> None:
    """
    Run tests and handle errors
    """
    try:
        parsed_argv = parsing(sys.argv)
        dictionary = analyse_string(parsed_argv)
        print_result(dictionary)
    except AssertionError as error:
        print(f"AssertionError: {error}")
    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
