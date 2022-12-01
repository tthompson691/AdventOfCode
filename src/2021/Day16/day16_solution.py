from utils import read_input
from numpy import prod


def calculate_values(type_id, values):
    if type_id == 0:
        return sum(values)
    elif type_id == 1:
        if len(values) != 1:
            return prod(values)
        else:
            return values[0]
    elif type_id == 2:
        return min(values)
    elif type_id == 3:
        return max(values)
    elif type_id == 5:
        if values[0] > values[1]:
            return 1
        else:
            return 0
    elif type_id == 6:
        if values[0] < values[1]:
            return 1
        else:
            return 0
    elif type_id == 7:
        if values[0] == values[1]:
            return 1
        else:
            return 0


def pad_zeros(packet):
    while len(packet) % 4 != 0:
        packet = "0" + packet

    return packet


def parse_packet(packet, versions=0):
    if packet == "":
        print("d")
    end_of_packet = False
    version = int(packet[0:3], 2)
    versions += version
    type_id = int(packet[3:6], 2)
    # print(f"packet:{packet}\n\tversion:{version}")

    if type_id == 4:
        i = 6
        contents = ""
        while not end_of_packet:
            subpacket = packet[i : i + 5]
            contents += subpacket[1:5]
            if subpacket[0] == "0":
                end_of_packet = True

            i += 5

        value = int(contents, 2)

        return contents, i, versions, value

    else:
        length_id = int(packet[6], 2)
        net_contents = ""
        values = []
        if length_id == 0:
            total_length_bits = int(packet[7:22], 2)
            len_parsed = 22
            while len_parsed < total_length_bits + 22:
                contents, len_packet, versions, value = parse_packet(
                    packet[len_parsed:], versions=versions
                )
                len_parsed += len_packet
                net_contents += contents
                values.append(value)

            total_value = calculate_values(type_id, values)

            return net_contents, len_parsed, versions, total_value

        elif length_id == 1:
            total_num_subpackets = int(packet[7:18], 2)
            len_parsed = 18
            for i in range(0, total_num_subpackets):
                contents, len_packet, versions, value = parse_packet(
                    packet[len_parsed:], versions=versions
                )
                len_parsed += len_packet
                net_contents += contents
                values.append(value)

            total_value = calculate_values(type_id, values)

            return net_contents, len_parsed, versions, total_value


if __name__ == "__main__":
    inp = read_input("day16_input.txt")
    a = 0
    hex = inp[a]
    packet = bin(int(hex, 16))[2:]
    if hex[0] == "0":
        packet = "0000" + packet
    packet = pad_zeros(packet)
    print(inp[a])

    final, i, versions, values = parse_packet(packet)

    print(f"versions: {versions}")
    print(f"value: {values}")
