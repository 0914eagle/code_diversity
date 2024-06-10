
def get_min_and_max_numbers(L, D, X):
    for N in range(L, D+1):
        if sum(int(digit) for digit in str(N)) == X:
            M = N
            break
    else:
        return -1, -1
    
    for M in range(L, D+1):
        if sum(int(digit) for digit in str(M)) == X:
            break
    
    return N, M

def main():
    L, D, X = map(int, input().split())
    N, M = get_min_and_max_numbers(L, D, X)
    print(N)
    print(M)

if __name__ == '__main__':
    main()

