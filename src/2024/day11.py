from utils.utils import read_input


def blink(stone, num_blinks):
    if (stone, num_blinks) in CACHE:
        return CACHE[stone, num_blinks]

    if num_blinks != {1: 25, 2: 75}[PART]:
        if stone == 0:
            CACHE[stone, num_blinks] = blink(1, num_blinks + 1)
        elif len(str(stone)) % 2 == 0 and len(str(stone)) > 1:
            stone1 = int(str(stone)[: len(str(stone)) // 2])
            stone2 = int(str(stone)[len(str(stone)) // 2 :])
            CACHE[stone, num_blinks] = blink(stone1, num_blinks + 1) + blink(stone2, num_blinks + 1)
        else:
            CACHE[stone, num_blinks] = blink(stone * 2024, num_blinks + 1)
    else:
        if len(str(stone)) % 2 == 0 and len(str(stone)) > 1:
            CACHE[stone, num_blinks] = 2
        else:
            CACHE[stone, num_blinks] = 1

    return CACHE[stone, num_blinks]


stones = list(map(int, read_input(2024, 11, source="real")[0].split(" ")))

for PART in 1, 2:
    CACHE = {}
    res = 0
    print(f"PART {PART}: {sum(blink(stone, 1) for stone in stones)}")

# Works cited: discussion via slay the spire metaphors with MC
