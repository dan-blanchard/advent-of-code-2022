import argparse
import fileinput
from collections import deque
from itertools import islice


def sliding_window(iterable, n):
    """Taken from itertools docs example"""
    # sliding_window('ABCDEFG', 4) -> ABCD BCDE CDEF DEFG
    it = iter(iterable)
    window = deque(islice(it, n), maxlen=n)
    if len(window) == n:
        yield tuple(window)
    for x in it:
        window.append(x)
        yield tuple(window)


def sliding_sum(*, num_list, n):
    return [sum(window) for window in sliding_window(num_list, n)]


def count_increasing(num_list):
    """Count how many numbers in list of numbers are larger than the previous"""
    return sum(
        (y > x for y, x in zip(reversed(num_list), islice(reversed(num_list), 1, None)))
    )


def get_groups(lines):
    groups = []
    group = []
    for line in lines:
        line = line.strip()
        if not line:
            groups.append(group)
            group = []
        else:
            group.append(int(line))
    return groups


def main():
    parser = argparse.ArgumentParser(
        description="Find group of items with highest sum given grouped list of numbers"
    )
    parser.add_argument(
        "files",
        metavar="FILE",
        nargs="*",
        help="Files to read. If empty, stdin is used.",
    )
    args = parser.parse_args()
    groups = get_groups(fileinput.input(args.files))
    sums = [sum(group) for group in groups]
    print(f"Max group: {max(sums)}")
    print(f"Top three: {sorted(sums, reverse=True)[:3]}")
    print(f"Sum of top three: {sum(sorted(sums, reverse=True)[:3])}")


if __name__ == "__main__":
    main()
