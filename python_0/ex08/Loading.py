import os
import sys
import time


def ft_tqdm(lst: range) -> None:
    """
    My own version of tqdm
    """
    try:
        start = time.perf_counter()
        total = len(lst)
        reserved = 5 + (len(str(total)) * 2 + 1) + 30
        for i, item in enumerate(lst, 1):
            terminal_width = os.get_terminal_size().columns + 3
            bar_size = max(10, terminal_width - reserved)
            progress = i / total

            elapsed_time = time.perf_counter() - start
            velocity = i / max(elapsed_time, 0.01)
            velocity = min(velocity, 999.99)
            eta = (total - i) / velocity

            filled = int(progress * bar_size)
            bar = "█" * filled + ' ' * (bar_size - filled)
            percentage = int(progress * 100)
            minutes = int(elapsed_time // 60)
            seconds = int(elapsed_time % 60)
            remaining_minutes = int(eta // 60)
            remaining_seconds = int(eta % 60)

            velocity_str = f"{velocity:6.2f}"
            line = (
                f"\r{percentage:3d}%|{bar}| {i:3d}/{total}"
                f"[{minutes:02}:{seconds:02}<"
                f"{remaining_minutes:02}:{remaining_seconds:02}"
                f", {velocity_str}it/s]"
            )
            line = line[:terminal_width - 1]
            sys.stdout.write(line)
            sys.stdout.flush()
            yield item

    except TypeError:
        total = None
        print()


def main():
    """
    Run tests and handle errors
    """
    print(ft_tqdm.__doc__)
    for i in ft_tqdm(range(1000)):
        time.sleep(0.02)


if __name__ == "__main__":
    main()
