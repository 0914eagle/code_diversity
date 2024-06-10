
def can_start_round_dance(p):
    n = len(p)
    if n == 1:
        return True
    if n == 2:
        return p[0] == p[1]
    if p[0] != 1:
        return False
    if p[n-1] != n:
        return False
    for i in range(1, n-1):
        if p[i] != p[i-1] + 1:
            return False
    return True

def solve(queries):
    for query in queries:
        n = int(query[0])
        p = list(map(int, query[1:]))
        if can_start_round_dance(p):
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    solve([[4, 1, 2, 3, 4], [3, 1, 3, 2], [5, 1, 2, 3, 5, 4], [1], [3, 2, 1, 5, 4]])

