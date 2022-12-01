from utils import read_input
from display_class import SingleDisplay

if __name__ == "__main__":
    ins = [
        (i.split("|")[0].split(), i.split("|")[1].split())
        for i in read_input("day8_input.txt")
    ]

    unique_outputs = len([j for i in ins for j in i[1] if len(j) in (2, 3, 4, 7)])

    print(f"PART 1: {unique_outputs}")

    # PART 2
    displays = [SingleDisplay(i[0], i[1]) for i in ins]

    final_sum = sum(display.output_number for display in displays)

    print(f"FINAL: {final_sum}")
