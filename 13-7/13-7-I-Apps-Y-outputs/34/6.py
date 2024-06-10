
def read_input():
    N = int(input())
    p = list(map(int, input().split()))
    return N, p

def is_sorted(p):
    return all(p[i] < p[i+1] for i in range(len(p)-1))

def swap(p, i, j):
    p[i], p[j] = p[j], p[i]

def solve(N, p):
    if is_sorted(p):
        return "YES"
    for i in range(N):
        for j in range(i+1, N):
            if p[i] > p[j]:
                swap(p, i, j)
                if is_sorted(p):
                    return "YES"
                swap(p, i, j)
    return "NO"

if __name__ == '__main__':
    N, p = read_input()
    print(solve(N, p))

