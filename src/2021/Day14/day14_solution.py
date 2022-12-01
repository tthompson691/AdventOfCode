from utils import read_input
import collections


def insert_the_things(running_str, _insertions, i=0):
    bits = [running_str[i : i + 2] for i in range(0, len(running_str))][:-1]
    new_str = "".join([f"{bit[0]}{insertions[bit]}" for bit in bits]) + running_str[-1]
    i += 1
    if i != 10:
        yield from insert_the_things(new_str, insertions, i)
    else:
        yield new_str


def insert_the_things2(bits_dict, _insertions, _char_counts, i=0):
    new_bits_dict = {}
    for bit in bits_dict:
        new_char = _insertions[bit]

        if new_char in char_counts:
            char_counts[new_char] = char_counts[new_char] + bits_dict[bit]
        else:
            char_counts[new_char] = bits_dict[bit]

        new_bit_l = f"{bit[0]}{new_char}"
        new_bit_r = f"{new_char}{bit[1]}"
        if new_bit_l in new_bits_dict:
            new_bits_dict[new_bit_l] += bits_dict[bit]
        else:
            new_bits_dict[new_bit_l] = bits_dict[bit]

        if new_bit_r in new_bits_dict:
            new_bits_dict[new_bit_r] += bits_dict[bit]
        else:
            new_bits_dict[new_bit_r] = bits_dict[bit]

    i += 1
    if i != 40:
        return insert_the_things2(new_bits_dict, _insertions, _char_counts, i)
    else:
        return _char_counts


if __name__ == "__main__":
    inp = read_input("day14_input.txt")
    start_str = inp[0]
    insertions = {i.split(" -> ")[0]: i.split(" -> ")[1] for i in inp[2:]}

    final_str = insert_the_things(running_str=start_str, _insertions=insertions)
    b = list(final_str)[0]
    a = collections.Counter(b)
    print(f"part 1: {a.most_common()[0][1] - a.most_common()[-1][1]}")

    # part 2
    bits2 = set([start_str[i : i + 2] for i in range(0, len(start_str))][:-1])
    bits2_dict = {bit2: start_str.count(bit2) for bit2 in bits2}
    char_counts = {char: start_str.count(char) for char in set(start_str)}
    char_counts = insert_the_things2(bits2_dict, insertions, char_counts)

    print(f"part 2: {max(char_counts.values()) - min(char_counts.values())}")
