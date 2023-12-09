from utils.utils import pull_input_directly

def calc_derivatives(all_seqs):
    cur_seq = all_seqs[-1]
    newseq = [cur_seq[i] - cur_seq[i - 1] for i in range(1, len(cur_seq))]
    if set(newseq) != {0}:
        all_seqs.append(newseq)
        return calc_derivatives(all_seqs)

    return all_seqs

def get_last_numbers(all_seqs):
    all_seqs.reverse()
    for i in range(1, len(all_seqs)):
        all_seqs[i].append(all_seqs[i-1][-1] + all_seqs[i][-1])
        all_seqs[i] = [all_seqs[i][0] - all_seqs[i-1][0]] + all_seqs[i]

    return all_seqs

if __name__ == "__main__":
    inp = pull_input_directly(2023, 9)[:-1]

    p1 = p2 = 0
    for sequence in inp:
        sequence = list(map(int, sequence.split(" ")))
        allseqs = calc_derivatives([sequence])
        allseqs = get_last_numbers(allseqs)

        p1 += allseqs[-1][-1]
        p2 += allseqs[-1][0]

    print(f"PART 1: {p1}")
    print(f"PART 2: {p2}")
