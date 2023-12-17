import requests
from utils.config import session_id
import os


def read_input(file, delimiter="\\n"):
    with open(file, "r") as f:
        return f.read().split(delimiter)


def pull_input_directly(year, day, mode="real", delimiter="\\n"):
    if mode == "real":
        url = f"https://adventofcode.com/{year}/day/{day}/input"
        session = {"session": session_id}
        r = requests.get(url, cookies=session, verify=False)

        if delimiter is not None:
            return str(r.content).strip("b'").split(delimiter)

        return str(r.content).strip("b'")
    else:
        src_path = os.path.abspath(os.path.join(__file__, "..", ".."))
        with open(os.path.join(src_path, f"{year}/examples/day{day}samp.txt"), "r") as f:
            return f.read().splitlines()
