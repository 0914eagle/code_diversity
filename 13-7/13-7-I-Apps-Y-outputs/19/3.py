
def get_input():
    N = int(input())
    A = list(map(int, input().split()))
    return N, A

def solve(N, A):
    max_diff = 0
    for i in range(N):
        for j in range(i+1, N):
            diff = abs(A[i] - A[j])
            if diff > max_diff:
                max_diff = diff
    return max_diff

def main():
    N, A = get_input()
    print(solve(N, A))

if __name__ == '__main__':
    main()

