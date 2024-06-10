
def find_min_max(L, D, X):
    # find the minimum number N such that L <= N <= D and the sum of its digits is X
    N = find_min(L, D, X)
    
    # find the maximum number M such that L <= M <= D and the sum of its digits is X
    M = find_max(L, D, X)
    
    return N, M

def find_min(L, D, X):
    # initialize the minimum number N to L
    N = L
    
    # loop through all numbers between L and D, inclusive
    for i in range(L, D+1):
        # check if the sum of the digits of the current number is X
        if sum(map(int, str(i))) == X:
            # if so, update the minimum number N
            N = i
            break
    
    return N

def find_max(L, D, X):
    # initialize the maximum number M to D
    M = D
    
    # loop through all numbers between L and D, inclusive
    for i in range(D, L-1, -1):
        # check if the sum of the digits of the current number is X
        if sum(map(int, str(i))) == X:
            # if so, update the maximum number M
            M = i
            break
    
    return M

if __name__ == '__main__':
    L, D, X = map(int, input().split())
    N, M = find_min_max(L, D, X)
    print(N)
    print(M)

