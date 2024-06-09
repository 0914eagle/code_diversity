
def get_minimum_moves(a, m):
    n = len(a)
    c = [0] * m
    for i in range(n):
        c[a[i] % m] += 1
    moves = 0
    for i in range(m):
        if c[i] != n // m:
            moves += abs(c[i] - n // m)
    return moves

def get_modified_array(a, m):
    n = len(a)
    c = [0] * m
    for i in range(n):
        c[a[i] % m] += 1
    modified_array = []
    for i in range(m):
        for j in range(c[i], n // m + c[i]):
            modified_array.append((j + 1) % m)
    return modified_array

if __name__ == '__main__':
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    print(get_minimum_moves(a, m))
    print(*get_modified_array(a, m))

