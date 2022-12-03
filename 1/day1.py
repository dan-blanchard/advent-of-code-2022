import argparse
import fileinput


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
