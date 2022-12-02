from utils.utils import pull_input_directly


def part_1(rounds, winkeys, rps_scores):
    drawkeys = {"A": "X", "B": "Y", "C": "Z"}
    score = 0
    
    for r in rounds:
        opponent = r[0]
        me = r[-1]
        
        if drawkeys[opponent] == me:
            # draw
            score += 3 + rps_scores[me]
        elif winkeys[opponent] == me:
            # win
            score += 6 + rps_scores[me]
        else:
            # loss
            score += rps_scores[me]
        
    return score

def part_2(rounds, winkeys, rps_scores):
    all_outcomes = {
        "X": {"A": "Z", "B": "X", "C": "Y", "val": 0},
        "Y": {"A": "X", "B": "Y", "C": "Z", "val": 3},
        "Z": winkeys
    }
    
    return sum(rps_scores[all_outcomes[r[-1]][r[0]]] + all_outcomes[r[-1]]["val"] for r in rounds)
            

if __name__ == "__main__":
    rounds = pull_input_directly(2022, 2)[:-1]
    winkeys = {"A": "Y", "B": "Z", "C": "X", "val": 6}
    rps_scores = {"X": 1, "Y": 2, "Z": 3}

    part1_score = part_1(rounds, winkeys, rps_scores)
    
    part2_score = part_2(rounds, winkeys, rps_scores)
    
    print(part2_score)
