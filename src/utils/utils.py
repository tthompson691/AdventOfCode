import requests
from utils.config import session_id


def read_input(file, delimiter="\\n"):
    with open(file, "r") as f:
        return f.read().split(delimiter)


def pull_input_directly(year, day, delimiter="\\n"):
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    session = {"session": session_id}
    r = requests.get(url, cookies=session, verify=False)

    if delimiter is not None:
        return str(r.content).strip("b'").split(delimiter)
    
    return str(r.content).strip("b'")
