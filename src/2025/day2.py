from utils.utils import read_input


def p2_check(val):
    stepsize = 1
    val = str(val)
    while stepsize <= len(val) // 2:
        splits = [val[a:a+stepsize] for a in range(0, len(val), stepsize)]
        if len(set(splits)) == 1:
            return True
        stepsize += 1
        
    return False
            
            
def p1_check(val):
    val = str(val)
    middle_index = int(len(val) / 2)
    if val[:middle_index] == val[int(middle_index):]:
        return True
    
    return False
    
    
def day2(input_data):
    id_ranges = [range(int(x.split("-")[0]), int(x.split("-")[1])+1)for x in input_data.split(",")]
    p1_res = 0
    p2_res = 0
    for id_range in id_ranges:
        for val in id_range:
            if p1_check(val):
                p1_res += val
            if p2_check(val):
                p2_res += val
            

    print(f"Part 1: {p1_res}")
    print(f"Part 2: {p2_res}")
                


if __name__ == "__main__":
    input_data = read_input(2025, 2, source="real")[0]
    day2(input_data)