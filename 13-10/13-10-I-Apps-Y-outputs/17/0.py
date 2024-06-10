
def read_input():
    N = int(input())
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))
    return N, P, Q

def lexicographically_smaller(P, Q):
    for i in range(len(P)):
        if P[i] != Q[i]:
            return P[i] < Q[i]
    return False

def find_index(P, Q, N):
    count = 0
    for i in range(1, N+1):
        p = [j for j in range(1, N+1) if j != i]
        if lexicographically_smaller(p, Q):
            count += 1
    return count + 1

def solve(N, P, Q):
    a = find_index(P, Q, N)
    b = find_index(Q, P, N)
    return abs(a - b)

if __name__ == '__main__':
    N, P, Q = read_input()
    print(solve(N, P, Q))

