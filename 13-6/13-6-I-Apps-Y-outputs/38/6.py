
def get_cost(A, N):
    # Calculate the cost of traveling from point 0 to point A[i]
    cost = [0]
    for i in range(1, N):
        cost.append(cost[i-1] + abs(A[i-1] - A[i]))
    
    # Calculate the cost of traveling from point A[i] to point 0
    cost.append(cost[N-1] + abs(A[N-1] - 0))
    
    return cost

def solve(A, N):
    # Get the cost of traveling for each spot
    cost = get_cost(A, N)
    
    # Calculate the total cost of travel for each spot
    total_cost = [0] * N
    for i in range(1, N):
        total_cost[i] = cost[i] + cost[i+1]
    
    return total_cost

if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    print(*solve(A, N))

