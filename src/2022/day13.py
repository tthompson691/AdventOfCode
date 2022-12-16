from utils.utils import pull_input_directly

if __name__ == "__main__":
    packets = pull_input_directly(2022, 13, delimiter="\\n\\n")

    packet_pairs = [
        (eval(p.split("\\n")[0]), eval(p.split("\\n")[1]))
        for p in packets
    ]

    for pp in packet_pairs:
        pass