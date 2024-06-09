
def is_increasing(seq):
    return all(seq[i] < seq[i+1] for i in range(len(seq)-1))

def is_decreasing(seq):
    return all(seq[i] > seq[i+1] for i in range(len(seq)-1))

def find_sequences(seq):
    n = len(seq)
    for i in range(n):
        for j in range(i+1, n):
            if is_increasing(seq[i:j]) and is_decreasing(seq[j:n]):
                return True, seq[i:j], seq[j:n]
    return False, [], []

def solve(seq):
    result = find_sequences(seq)
    if result[0]:
        return "YES\n" + " ".join(str(int(x in result[1])) for x in seq)
    else:
        return "NO"

if __name__ == '__main__':
    n = int(input())
    seq = list(map(int, input().split()))
    print(solve(seq))

