import argparse
import fileinput

A_ORD = ord("A")
X_ORD = ord("X")


def score_round(line, second_is_outcome):
    opponent, own = line.split()
    opponent_shape = ord(opponent) - A_ORD
    # If the second field on the line is actually the outcome,
    # and not what we should play, figure out what we should play
    if second_is_outcome:
        if own == "X":
            own_shape = (opponent_shape - 1) % 3
        elif own == "Y":
            own_shape = opponent_shape
        else:
            own_shape = (opponent_shape + 1) % 3
    else:
        own_shape = ord(own) - X_ORD
    # Win
    if own_shape == (opponent_shape + 1) % 3:
        score = 6
    # Draw
    elif own_shape == opponent_shape:
        score = 3
    # Lose
    else:
        score = 0
    return score + (own_shape + 1)


def main():
    parser = argparse.ArgumentParser(
        description="Score a strategy for playing Rock-Paper-Scissors"
    )
    parser.add_argument(
        "files",
        metavar="FILE",
        nargs="*",
        help="Files to read. If empty, stdin is used.",
    )
    args = parser.parse_args()
    lines = [line.strip() for line in fileinput.input(args.files)]
    round_scores = [score_round(line, False) for line in lines]
    print(f"Part A score sum: {sum(round_scores)}")
    round_scores = [score_round(line, True) for line in lines]
    print(f"Part B score sum: {sum(round_scores)}")


if __name__ == "__main__":
    main()
