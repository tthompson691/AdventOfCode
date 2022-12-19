from utils.utils import pull_input_directly, read_input


def compare(pp_l, pp_r):
    if type(pp_l) == list and type(pp_r) == int:
        pp_r = [pp_r]
    elif type(pp_l) == int and type(pp_r) == list:
        pp_l = [pp_l]
    elif type(pp_l) == int and type(pp_r) == int:
        if pp_l > pp_r:
            return False
        elif pp_l < pp_r:
            return True
    else:
        if len(pp_l) == 0 and len(pp_r) != 0:
            return True
        for j in range(len(pp_l)):
            try:
                return compare(pp_l[j], pp_r[j])
            except IndexError:
                return False


if __name__ == "__main__":
    # packets = pull_input_directly(2022, 13, delimiter="\\n\\n")
    packets = read_input("day13tst.txt", "\n\n")
    packet_pairs = [
        (eval(p.split("\n")[0]), eval(p.split("\n")[1]))
        for p in packets
    ]

    p1_ans = 0
    for i, packpair in enumerate(packet_pairs):
        if compare(packpair[0], packpair[1]):
            p1_ans += i + 1

    print(p1_ans)