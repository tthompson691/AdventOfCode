import requests
from utils.config import session_id


def read_input(file):
    with open(file, "r") as f:
        return f.read().split("\n")


def pull_input_directly(year, day, split_newlines=True):
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    session = {"session": session_id}
    r = requests.get(url, cookies=session, verify=False)

    if split_newlines:
        return str(r.content).strip("b'").split("\\n")
    
    return str(r.content).strip("b'")
