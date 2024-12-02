import os

import requests

from utils.config import session_id


def read_input(year: int, day: int, delimiter="\n", source="real"):
    sample_inputs_path = os.path.abspath(os.path.join(__file__, "..", "..", "sample_inputs"))

    if source == "sample":
        with open(os.path.join(sample_inputs_path, f"{year}_{day}.txt")) as f:
            return f.read().split("\n")
    elif source == "real":
        return pull_input_directly(year, day)


def pull_input_directly(year, day):
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    session = {"session": session_id}
    r = requests.get(url, cookies=session, verify=False)
    return str(r.content).strip("b'").split("\\n")[:-1]

    # return str(r.content).strip("b'")[:-1]
