
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
    
    # Initialize the minimum cost to travel
    min_cost = cost[0]
    
    # Iterate through each spot and calculate the total cost of travel when that spot is canceled
    for i in range(1, N+1):
        total_cost = 0
        for j in range(N+1):
            if j != i:
                total_cost += cost[j]
        min_cost = min(min_cost, total_cost)
    
    return min_cost

def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(solve(A, N))

if __name__ == '__main__':
    main()

