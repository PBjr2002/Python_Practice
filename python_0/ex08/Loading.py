import os
import sys
import time

def ft_tqdm(lst: range) -> None:
    """
    My own version of tqdm
    """


def main():
    """
    Run tests and handle errors
    """
    print(ft_tqdm.__doc__)
    for i in ft_tqdm(range(10000)):
        time.sleep(0.02)


if __name__ == "__main__":
    main()