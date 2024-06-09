
def find_pairs(n):
    pairs = []
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            pairs.append((i, j))
    return pairs

def solve(n):
    pairs = find_pairs(n)
    q = len(pairs)
    print(q)
    for pair in pairs:
        print(pair[0], pair[1])

if __name__ == '__main__':
    n = int(input())
    solve(n)

