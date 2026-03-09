import sys

def filter_string(av: list):
    """
    Used to parse the input received and print
    the respective output
    """
    ac = len(av)
    if ac != 3:
        raise AssertionError("the arguments are bad")

    try:
        size = int(av[2])
    except ValueError:
        raise AssertionError("the arguments are bad")
    
    splited_string = av[1].split()

    res = [s for s in splited_string if (lambda x: len(x) > size)(s)]
    print(res)


def main() -> None:
    """
    Run tests and handle errors
    """
    try:
        filter_string(sys.argv)
    except AssertionError as error:
        print(f"AssertionError: {error}")


if __name__ == "__main__":
    main()