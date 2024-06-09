
def get_input():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    return N, M, A

def solve(N, M, A):
    days_spent = 0
    for i in range(M):
        days_spent += A[i]
        if days_spent > N:
            return -1
    return N - days_spent

def main():
    N, M, A = get_input()
    print(solve(N, M, A))

if __name__ == '__main__':
    main()

