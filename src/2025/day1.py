from utils.utils import read_input


def day1(input_data):
    turns = [int(x[1:]) if x[0] == "R" else -int(x[1:]) for x in input_data]
    position = 50
    zeros = 0
    p2_zeros = 0
    for turn in turns:
        p2_zeros += abs(turn) // 100
        remainder = turn % 100 if turn > 0 else turn % -100
        if position + remainder not in range(0, 101) and position != 0:
            p2_zeros += 1
        elif position + remainder in (100, 0):
            p2_zeros += 1
            zeros += 1
        position = (position + turn) % 100
    
    print(f"Total zeros: {zeros}")
    print(f"Total p2 zeros: {p2_zeros}")

if __name__ == "__main__":
    input_data = read_input(2025, 1, source="real")
    day1(input_data)
    