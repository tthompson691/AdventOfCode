from utils.utils import read_input


def validate_report(diffs):
    return (all([d > 0 for d in diffs]) or all([d < 0 for d in diffs])) and all(
        [1 <= abs(d) <= 3 for d in diffs]
    )


def get_report_diffs(report):
    return [report[i] - report[i - 1] for i in range(1, len(report))]


def run_one_report(_report, retry=False, drop_index=0):
    diffs = get_report_diffs(_report)
    if validate_report(diffs):
        if not retry:
            return "p1"
        else:
            return "p2"
    else:
        if drop_index <= len(_report):
            _report = report[:drop_index] + report[drop_index + 1 :]
            return run_one_report(_report, retry=True, drop_index=drop_index + 1)
        else:
            return None


if __name__ == "__main__":
    reports = [list(map(int, r.split(" "))) for r in read_input(2024, 2, source="real")]
    p1_safe_reports = p2_safe_reports = 0
    # look. I'm well aware I could list comprehend this. Shush your mouth. But list comprehension
    # breaks the func's reference the global variable report. I'd say I'll fix it later but
    # I probably won't
    res = []
    for report in reports:
        res.append(run_one_report(report))

    print(f"PART 1: {len([r for r in res if r == 'p1'])}")
    print(f"PART 2: {len([r for r in res if r in ['p1', 'p2']])}")
