
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
    for i in range(len(seq)):
        if is_decreasing(seq[i:]):
            return seq[i:]
    return []

def solve(a):
    increasing = find_increasing_sequence(a)
    decreasing = find_decreasing_sequence(a)
    if len(increasing) == 0 or len(decreasing) == 0:
        return "NO"
    res = [0] * len(a)
    for i in range(len(increasing)):
        res[i] = 0
    for i in range(len(decreasing)):
        res[len(a)-i-1] = 1
    return "YES\n" + " ".join(map(str, res))

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(a))

