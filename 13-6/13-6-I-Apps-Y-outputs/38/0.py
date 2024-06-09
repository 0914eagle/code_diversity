
def get_input():
    N = int(input())
    A = list(map(int, input().split()))
    return N, A

def get_cost(A, i):
    cost = 0
    for j in range(N):
        if j != i:
            cost += abs(A[j] - A[i])
    return cost

def solve(N, A):
    costs = []
    for i in range(N):
        costs.append(get_cost(A, i))
    return costs

if __name__ == '__main__':
    N, A = get_input()
    costs = solve(N, A)
    for cost in costs:
        print(cost)

