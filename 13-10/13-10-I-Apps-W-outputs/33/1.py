
def read_input():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    return N, K, A

def solve(N, K, A):
    pairs = []
    for i in range(N):
        for j in range(i+1, N):
            pairs.append(A[i] * A[j])
    pairs.sort()
    return pairs[K-1]

def main():
    N, K, A = read_input()
    print(solve(N, K, A))

if __name__ == '__main__':
    main()

