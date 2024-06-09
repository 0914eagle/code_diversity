
def is_increasing(seq):
    return all(seq[i] < seq[i+1] for i in range(len(seq)-1))

def is_decreasing(seq):
    return all(seq[i] > seq[i+1] for i in range(len(seq)-1))

def find_increasing_sequence(seq):
    for i in range(len(seq)):
        if is_increasing(seq[:i+1]):
            return seq[:i+1]
    return []

def find_decreasing_sequence(seq):
    for i in range(len(seq)-1, -1, -1):
        if is_decreasing(seq[i:]):
            return seq[i:]
    return []

def solve(seq):
    increasing_seq = find_increasing_sequence(seq)
    decreasing_seq = find_decreasing_sequence(seq)
    if len(increasing_seq) == 0 or len(decreasing_seq) == 0:
        return "NO"
    res = []
    for i in range(len(seq)):
        if seq[i] in increasing_seq:
            res.append(0)
        else:
            res.append(1)
    return "YES\n" + " ".join(map(str, res))

if __name__ == '__main__':
    n = int(input())
    seq = list(map(int, input().split()))
    print(solve(seq))

