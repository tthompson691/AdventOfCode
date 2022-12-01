from utils import pull_input_directly
import numpy as np


def determine_pixel(_slice, _on_border):
    bin_dict = {".": "0", "#": "1"}
    if not on_border:
        linear_str = "".join([bin_dict[y] for x in _slice for y in x])
    else:
        linear_str = "".join(bin_dict[_slice[1, 1]] for x in _slice for y in x)

    res_int = int(linear_str, 2)
    return algo_str[res_int]


if __name__ == "__main__":
    inp = pull_input_directly(2021, 20)
    padding = 100
    algo_str = inp[0][2:]
    img_list = [
        ["." for p in range(padding)] + [i for i in j] + ["." for p in range(padding)]
        for j in inp[2:-1]
    ]

    new_len = len(img_list[0])

    img_list = (
        [["." for d in range(new_len)] for p in range(padding)]
        + img_list
        + [["." for d in range(new_len)] for p in range(padding)]
    )
    img = np.array(img_list)
    img_enhanced = np.copy(img)

    row_indices = col_indices = range(1, len(img_list[0]))
    for q in range(0, 50):
        for i in row_indices:
            for j in col_indices:
                if i == 1 or i == max(row_indices) or j == 1 or j == max(row_indices):
                    on_border = True
                else:
                    on_border = False

                slice = img[i - 1 : i + 2, j - 1 : j + 2]
                pix = determine_pixel(slice, on_border)
                img_enhanced[i, j] = pix

        img = np.copy(img_enhanced)

    print((img == "#").sum())
