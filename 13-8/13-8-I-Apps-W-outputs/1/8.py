
def is_increasing(seq):
    return all(seq[i] <= seq[i+1] for i in range(len(seq)-1))

def get_replacement(seq, candidates):
    result = []
    for i in range(len(seq)):
        if seq[i] == 0:
            result.append(candidates.pop())
        else:
            result.append(seq[i])
    return result

def solve(n, k, seq, candidates):
    result = get_replacement(seq, candidates)
    return "Yes" if not is_increasing(result) else "No"

if __name__ == '__main__':
    n, k = map(int, input().split())
    seq = list(map(int, input().split()))
    candidates = list(map(int, input().split()))
    print(solve(n, k, seq, candidates))

