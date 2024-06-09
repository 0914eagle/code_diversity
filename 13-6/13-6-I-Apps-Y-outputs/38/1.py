
def get_input():
    N = int(input())
    A = list(map(int, input().split()))
    return N, A

def solve(N, A):
    total_cost = [0] * (N + 1)
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i != j:
                total_cost[i] += abs(A[i - 1] - A[j - 1])
    return total_cost

def main():
    N, A = get_input()
    total_cost = solve(N, A)
    for i in range(1, N + 1):
        print(total_cost[i])

if __name__ == '__main__':
    main()

