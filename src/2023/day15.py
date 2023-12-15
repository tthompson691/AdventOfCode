from utils import pull_input_directly
from math import prod

class Box:
    def __init__(self, num):
        self.num = num
        self.lenses = []

    def add_lens(self, newlens):
        for i, l in enumerate(self.lenses):
            if newlens[0] == l[0]:
                self.lenses[i] = newlens
                return

        self.lenses.append(newlens)

    def remove_lens(self, lens_name):
        for l in self.lenses:
            if l[0] == lens_name:
                self.lenses.remove(l)

    def calc_focusing_power(self):
        return sum([(1 + self.num) * (i+1) * l[1] for i, l in enumerate(self.lenses)])

def hash_it(char, cur_sum=0):
    return (cur_sum + ord(char)) * 17 % 256

def hash_all(s):
    cur_sum = 0
    for char in s:
        cur_sum = hash_it(char, cur_sum)

    return cur_sum

def find_matching_box(boxes: list[Box], lens_label):
    for i, box in enumerate(boxes):
        if lens_label in box.labels:
            return i

    return None

if __name__ == "__main__":
    sequence = pull_input_directly(2023, 15, mode="real", delimiter=",")
    sequence[-1] = sequence[-1].removesuffix("\\n")

    print(f"PART 1: {sum(map(hash_all, sequence))}")

    ## PART 2 ##
    boxes = [Box(num=i) for i in range(256)]
    box_num = 0
    for s in sequence:
        if "=" in s:
            lens_name, length = s.split("=")
            matching_box = hash_all(lens_name)
            boxes[matching_box].add_lens((lens_name, int(length)))
        elif "-" in s:
            lens_name = s.removesuffix("-")
            matching_box = hash_all(lens_name)
            boxes[matching_box].remove_lens(lens_name)

    # p2 = sum([b.calc_focusing_power() for b in boxes])
    print(f"PART 2: {sum([b.calc_focusing_power() for b in boxes])}")
