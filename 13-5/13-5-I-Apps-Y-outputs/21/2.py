
def is_strictly_increasing(seq):
    return all(seq[i] < seq[i+1] for i in range(len(seq)-1))

def is_strictly_decreasing(seq):
    return all(seq[i] > seq[i+1] for i in range(len(seq)-1))

def find_initial_sequences(a):
    n = len(a)
    for i in range(n):
        for j in range(i+1, n):
            increasing = a[:i]
            decreasing = a[i:j+1]
            remaining = a[j+1:]
            if is_strictly_increasing(increasing) and is_strictly_decreasing(decreasing):
                return increasing, decreasing
    return None, None

def solve(a):
    increasing, decreasing = find_initial_sequences(a)
    if increasing is None or decreasing is None:
        return "NO"
    res = [0]*len(a)
    for i in range(len(increasing)):
        res[i] = 0
    for i in range(len(decreasing)):
        res[len(increasing)+i] = 1
    return "YES\n" + " ".join(map(str, res))

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(a))

