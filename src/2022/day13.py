from utils import pull_input_directly


def compare(pp_l, pp_r):
    if isinstance(pp_l, list) and isinstance(pp_r, int):
        pp_r = [pp_r]
        return compare(pp_l, pp_r)
    elif isinstance(pp_l, int) and isinstance(pp_r, list):
        pp_l = [pp_l]
        return compare(pp_l, pp_r)
    elif isinstance(pp_l, int) and isinstance(pp_r, int):
        if pp_l > pp_r:
            return False
        elif pp_l < pp_r:
            return True
        else:
            return None
    else:
        if len(pp_r) == 0 and len(pp_l) != 0:
            return False
        for j in range(len(pp_r)):
            try:
                ans = compare(pp_l[j], pp_r[j])
                if ans is not None:
                    return ans
                else:
                    continue
            except IndexError:
                return True


if __name__ == "__main__":
    packet_pairs = [
        (eval(p.split("\\n")[0]), eval(p.split("\\n")[1]))
        for p in pull_input_directly(2022, 13, delimiter="\\n\\n")
    ]

    p2_packets = [eval(p) for p in pull_input_directly(2022, 13) if p != ""] + [[[2]], [[6]]]

    p1_ans = 0
    for i, packpair in enumerate(packet_pairs):
        if compare(packpair[0], packpair[1]):
            p1_ans += i + 1

    print(p1_ans)

    ordered_packets = [p2_packets[0]]
    for p in p2_packets[1:]:
        x = 0
        for x, op in enumerate(ordered_packets):
            if compare(p, op):
                ordered_packets = ordered_packets[:x] + [p] + ordered_packets[x:]
                break
            elif x == len(ordered_packets) - 1:
                ordered_packets = ordered_packets + [p]
            else:
                x += 1

    print((ordered_packets.index([[2]]) + 1) * (ordered_packets.index([[6]]) + 1))
