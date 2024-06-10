
def get_min_number(L, D, X):
    for N in range(L, D+1):
        if sum(int(i) for i in str(N)) == X:
            return N
    return -1

def get_max_number(L, D, X):
    for M in range(L, D+1):
        if sum(int(i) for i in str(M)) == X:
            return M
    return -1

if __name__ == '__main__':
    L, D, X = map(int, input().split())
    print(get_min_number(L, D, X))
    print(get_max_number(L, D, X))

