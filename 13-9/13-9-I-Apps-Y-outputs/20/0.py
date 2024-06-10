
def get_min_num(L, D, X):
    for N in range(L, D+1):
        if sum(int(digit) for digit in str(N)) == X:
            return N
    return -1

def get_max_num(L, D, X):
    for M in range(L, D+1):
        if sum(int(digit) for digit in str(M)) == X:
            return M
    return -1

if __name__ == '__main__':
    L = int(input())
    D = int(input())
    X = int(input())
    print(get_min_num(L, D, X))
    print(get_max_num(L, D, X))

