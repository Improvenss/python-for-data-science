# Allowed functions : None
# import os as os

# LINK: https://www.geeksforgeeks.org/enumerate-in-python/
def ft_tqdm(lst: range) -> None:
    """
    Custom implementation of tqdm using yield operator.

    Args:
        lst (range): The iterable range.

    Yields:
        int: Each element from the iterable range while displaying progress.
    """
    total = len(lst)
    bar_length = 60
    # column, row = os.get_terminal_size()
    # print("column:", column)
    # print("row:", row)
    for index, elem in enumerate(lst, start=1):
        percent = index / total
        bar = "█" * int(percent * bar_length)
        spaces = " " * (bar_length - len(bar))
        print(
            f"\r{percent:>4.0%}|{bar}{spaces}| {index}/{total}",
            end="",
            flush=True,
        )
        yield elem
    print()
