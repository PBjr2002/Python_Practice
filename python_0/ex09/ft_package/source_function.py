import sys


def convert_to_morse(input) -> str:
    """
    Converts the input received to morse code
    and returns it in a string
    """
    NESTED_MORSE = {
        " ": "/ ",
        "A": ".- ", "B": "-... ", "C": "-.-. ",
        "D": "-.. ", "E": ". ", "F": "..-. ",
        "G": "--. ", "H": ".... ", "I": ".. ",
        "J": ".--- ", "K": "-.- ", "L": ".-.. ",
        "M": "-- ", "N": "-. ", "O": "--- ",
        "P": ".--. ", "Q": "--.- ", "R": ".-. ",
        "S": "... ", "T": "- ", "U": "..- ",
        "V": "...- ", "W": ".-- ", "X": "-..- ",
        "Y": "-.-- ", "Z": "--.. ", "Ç": "-.-.. ",
        "1": ".---- ", "2": "..--- ", "3": "...-- ",
        "4": "....- ", "5": "..... ", "6": "-.... ",
        "7": "--... ", "8": "---.. ", "9": "----. ",
        "0": "----- ",
    }
    converted_string = ""
    for char in input:
        converted_string += NESTED_MORSE[char.upper()]
    return converted_string


def verify_input(input) -> bool:
    """
    Validates the input received
    """
    for char in input:
        if not (char.isalnum() and char.isspace()):
            return False
    return True


def main() -> None:
    """
    Run tests and handle errors
    """
    try:
        ac = len(sys.argv)
        assert ac == 2, "the arguments are bad"
        if not verify_input(sys.argv[1]):
            raise AssertionError("the arguments are bad")
        converted_string = convert_to_morse(sys.argv[1])
        print(converted_string)
    except AssertionError as error:
        print(f"AssertionError: {error}")


if __name__ == "__main__":
    main()
