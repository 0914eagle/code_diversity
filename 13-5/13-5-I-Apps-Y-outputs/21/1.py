
def is_strictly_increasing(seq):
    return all(seq[i] < seq[i+1] for i in range(len(seq)-1))

def is_strictly_decreasing(seq):
    return all(seq[i] > seq[i+1] for i in range(len(seq)-1))

def find_increasing_sequence(seq):
    for i in range(len(seq)):
        if is_strictly_increasing(seq[:i+1]):
            return seq[:i+1]
    return []

def find_decreasing_sequence(seq):
    for i in range(len(seq)):
        if is_strictly_decreasing(seq[:i+1]):
            return seq[:i+1]
    return []

def solve(seq):
    increasing_seq = find_increasing_sequence(seq)
    decreasing_seq = find_decreasing_sequence(seq)
    if increasing_seq and decreasing_seq:
        return "YES", [1 if i in increasing_seq else 0 for i in seq]
    else:
        return "NO", []

if __name__ == '__main__':
    n = int(input())
    seq = list(map(int, input().split()))
    print(solve(seq))

