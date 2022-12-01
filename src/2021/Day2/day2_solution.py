

if __name__ == "__main__":
    with open("day2_input.txt", "r") as f:
        commands = f.read()
        commands = commands.split("\n")

    split_commands = [(command.split(" ")[0], int(command.split(" ")[1])) for command in commands]

    forwards = [command[1] for command in split_commands if command[0] == "forward"]
    total_forward = sum(forwards)

    ups = [command[1] for command in split_commands if command[0] == "up"]
    downs = [command[1] for command in split_commands if command[0] == "down"]
    net_depth = sum(downs) - sum(ups)

    print(f"forward movement: {total_forward}\nnet depth:{net_depth}")
    print(f"product: {total_forward * net_depth}")

    ## part 2 ##
    aim = 0
    horizontal = 0
    depth = 0
    for command in split_commands:
        if command[0] == "forward":
            horizontal += command[1]
            depth += aim * command[1]
        elif command[0] == "up":
            aim -= command[1]
        elif command[0] == "down":
            aim += command[1]

    print("#### PART 2 #####\n")
    print(f"horizontal: {horizontal}")
    print(f"depth: {depth}")
    print(f"PRODUCT: {horizontal * depth}")