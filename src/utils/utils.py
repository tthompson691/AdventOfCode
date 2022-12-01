import requests
from config import session_id


def read_input(file):
    with open(file, "r") as f:
        return f.read().split("\n")


def pull_input_directly(year, day):
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    session = {"session": session_id}
    r = requests.get(url, cookies=session, verify=False)

    return str(r.content).split("\\n")
