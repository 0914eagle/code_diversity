
def get_cost(A, N):
    # Calculate the cost of traveling from spot i to spot i+1
    cost = [0] * (N+1)
    for i in range(N-1):
        cost[i+1] = abs(A[i] - A[i+1])
    
    # Calculate the total cost of traveling from spot 0 to spot N
    total_cost = 0
    for i in range(N):
        total_cost += cost[i]
    
    return total_cost

def solve(A, N):
    # Calculate the cost of traveling from spot i to spot i+1
    cost = [0] * (N+1)
    for i in range(N-1):
        cost[i+1] = abs(A[i] - A[i+1])
    
    # Calculate the total cost of traveling from spot 0 to spot N
    total_cost = 0
    for i in range(N):
        total_cost += cost[i]
    
    # Find the minimum total cost by canceling one spot
    min_cost = total_cost
    for i in range(N):
        min_cost = min(min_cost, total_cost - cost[i])
    
    return min_cost

if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    print(solve(A, N))

