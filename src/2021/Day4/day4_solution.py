import pandas as pd
from board_class import BingoBoard


if __name__ == "__main__":
    # read input
    with open("day4_input1.txt", "r") as f:
        calls = f.read().split(",")

    with open("day4_input2.txt", "r") as f:
        boards = f.read().split("\n\n")

    all_boards = [BingoBoard(board) for board in boards]
    board_count = len(all_boards)
    finished_boards = 0
    # PART 1
    for call in calls:
        for board in all_boards:
            if not board.has_bingo:
                board.check_space(call)
                is_bingo = board.check_bingo()

                if is_bingo:
                    finished_boards += 1
                    print("debug")

                if finished_boards == board_count:
                    print("debug")

    print("debug")
