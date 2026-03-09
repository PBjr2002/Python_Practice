def ft_filter(function, iterable):
    """
    ft_filter(function or None, iterable) --> filter object

    Return an iterator yielding those items of iterable for which function(item)
    is true. If function is None, return the items that are true.
    """
    if function is not None and not callable(function):
        raise TypeError("Function must be callable")

    try:
        iter(iterable)
    except TypeError:
        raise TypeError("Object must be iterable")
    
    if function is None:
        result = [x for x in iterable if x]
    else:
        result = [x for x in iterable if function(x)]
    yield from result


def test_function(character):
    """
    Function used to test the iteration
    """
    return character.isupper()


def main() -> None:
    """
    Run tests and handle errors
    """
    try:
        print(ft_filter.__doc__)
        test_object = "Sou Uma String"
        result = ft_filter(test_function, test_object)
        print(list(result))
    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()