UNIVERSAL_NUMS = {
    "vz": 1,
    "tvwxy": 2,
    "tvwzy": 3,
    "uwvz": 4,
    "tuwzy": 5,
    "tuwzyx": 6,
    "tvz": 7,
    "tuvwxyz": 8,
    "tuvwz": 9,
    "tuxyzv": 0,
}


class SingleDisplay:
    def __init__(self, inputs, outputs):
        self.inputs = inputs
        self.outputs = outputs
        self.segs = {
            "t": None,
            "u": None,
            "v": None,
            "w": None,
            "x": None,
            "y": None,
            "z": None,
        }

        self.nums = {
            1: None,
            2: None,
            3: None,
            4: None,
            5: None,
            6: None,
            7: None,
            8: None,
            9: None,
            0: None,
        }

        self.final_nums = self.establish_unique_numbers()

        self.output_number = self.decode_output()

    def establish_unique_numbers(self):
        self.nums[1] = [i for i in self.inputs if len(i) == 2][0]
        self.nums[4] = [i for i in self.inputs if len(i) == 4][0]
        self.nums[7] = [i for i in self.inputs if len(i) == 3][0]
        self.nums[8] = [i for i in self.inputs if len(i) == 7][0]

        self.segs["t"] = list(set(list(self.nums[7])) - set(list(self.nums[1])))[0]

        # 6 must be whichever input is len=6 and does not contain BOTH segs of the right vertical
        right_vertical = set(list(self.nums[1]))
        self.nums[6] = [
            i
            for i in self.inputs
            if len(i) == 6 and not right_vertical.issubset(set(list(i)))
        ][0]

        self.segs["z"] = list(
            set(list(self.nums[6])).intersection(set(list(self.nums[1])))
        )[0]
        self.segs["v"] = [i for i in list(right_vertical) if i != self.segs["z"]][0]

        self.nums[5] = [
            i
            for i in self.inputs
            if len(i) == 5 and self.segs["z"] in i and not self.segs["v"] in i
        ][0]
        self.nums[2] = [
            i
            for i in self.inputs
            if len(i) == 5 and self.segs["v"] in i and not self.segs["z"] in i
        ][0]
        self.nums[3] = [
            i
            for i in self.inputs
            if len(i) == 5 and self.segs["v"] in i and self.segs["z"] in i
        ][0]

        left_vertical = {"a", "b", "c", "d", "e", "f", "g"} - (set(list(self.nums[3])))

        self.nums[0] = [
            i
            for i in self.inputs
            if len(i) == 6
            and left_vertical.issubset(set(list(i)))
            and i not in self.nums.values()
        ][0]
        self.nums[9] = [i for i in self.inputs if i not in self.nums.values()][0]

        return {self.nums[k]: k for k in self.nums}

    def decode_output(self):
        final_output = ""
        for output in self.outputs:
            for k in self.final_nums:
                if set(list(output)) == set(list(k)):
                    final_output += str(self.final_nums[k])

        return int(final_output)
