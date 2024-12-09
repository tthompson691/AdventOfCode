from utils.utils import read_input

disk_map = read_input(2024, 9, source="sample")[0]

disk_str = ""
p1_raw_disk = []
p2_raw_disk = []
for pos in range(0, len(disk_map), 2):
    block_id = 0 if pos == 0 else int(pos / 2)
    filesize = int(disk_map[pos])
    free_space = 0 if pos >= len(disk_map) - 1 else int(disk_map[pos + 1])
    p2_raw_disk.append({"id": block_id, "size": filesize})
    p2_raw_disk.append({"id": ".", "size": free_space})
    [p1_raw_disk.append(block_id) for _ in range(filesize)]
    [p1_raw_disk.append(".") for _ in range(free_space)]

left = 0
right = len(p1_raw_disk) - 1
# PART 1
while left < right:
    if p1_raw_disk[left] == ".":
        p1_raw_disk[left] = p1_raw_disk[right]
        p1_raw_disk[right] = "."
        while p1_raw_disk[right] == ".":
            right -= 1

    left += 1

p1_raw_disk = [x for x in p1_raw_disk if x != "."]
print(f"PART 1: {sum(i * v for i, v in enumerate(p1_raw_disk))}")

# PART 2
while block_id >= 0:
    loc, file_ = [(loc, x) for loc, x in enumerate(p2_raw_disk) if x["id"] == block_id][0]
    i = 0
    while i < len(p2_raw_disk):
        if p2_raw_disk[i]["id"] == "." and p2_raw_disk[i]["size"] >= file_["size"] and i < loc:
            p2_raw_disk[i]["size"] -= file_["size"]
            p2_raw_disk[loc] = {"id": ".", "size": file_["size"]}
            p2_raw_disk = p2_raw_disk[:i] + [file_] + p2_raw_disk[i:]
            break
        i += 1

    block_id -= 1

p2_disk = []

for _file in p2_raw_disk:
    [p2_disk.append(_file["id"]) for _ in range(_file["size"])]


print(f"PART 2: {sum(i * v for i, v in enumerate(p2_disk) if v != '.')}")
