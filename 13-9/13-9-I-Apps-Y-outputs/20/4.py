
def find_min_number(L, D, X):
    for N in range(L, D+1):
        if sum(int(i) for i in str(N)) == X:
            return N
    return -1

def find_max_number(L, D, X):
    for M in range(D, L-1, -1):
        if sum(int(i) for i in str(M)) == X:
            return M
    return -1

if __name__ == '__main__':
    L, D, X = map(int, input().split())
    N = find_min_number(L, D, X)
    M = find_max_number(L, D, X)
    print(N)
    print(M)

