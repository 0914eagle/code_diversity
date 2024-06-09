
def check_pairs(pairs):
    n = len(pairs)
    for i in range(n):
        for j in range(i+1, n):
            if pairs[i][0] == pairs[j][0] or pairs[i][1] == pairs[j][1]:
                return True
    return False

def solve(n, m, pairs):
    if check_pairs(pairs):
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    n, m = map(int, input().split())
    pairs = []
    for i in range(m):
        a, b = map(int, input().split())
        pairs.append((a, b))
    print(solve(n, m, pairs))

