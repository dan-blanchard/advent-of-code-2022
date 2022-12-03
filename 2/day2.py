import argparse
import fileinput

A_ORD = ord("A")
X_ORD = ord("X")


def score_round1(line):
    opponent, own = line.split()
    opponent_shape = ord(opponent) - A_ORD
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


def score_round2(line):
    opponent, lose_draw_win = line.split()
    opponent_shape = ord(opponent) - A_ORD
    if lose_draw_win == "X":
        own_shape = (opponent_shape - 1) % 3
    elif lose_draw_win == "Y":
        own_shape = opponent_shape
    else:
        own_shape = (opponent_shape + 1) % 3
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
    round_scores = [score_round1(line) for line in lines]
    print(f"Part A score sum: {sum(round_scores)}")
    round_scores = [score_round2(line) for line in lines]
    print(f"Part B score sum: {sum(round_scores)}")


if __name__ == "__main__":
    main()
