from utils.utils import pull_input_directly 

def decrypt(stream, step):
    for i in range(len(stream)):
        if len(set(stream[i:i+step])) == step:
            return  i + step


if __name__ == "__main__":
    inp = pull_input_directly(2022, 6)[0]
    
    part1 = decrypt(inp, step=4)
    part2 = decrypt(inp, step=14)
    
    print(part1)
    print(part2)