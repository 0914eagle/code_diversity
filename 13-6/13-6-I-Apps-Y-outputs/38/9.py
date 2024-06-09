
def get_cost(A, N):
    # Calculate the total cost of travel when visiting each spot
    cost = [0] * (N + 1)
    for i in range(1, N + 1):
        cost[i] = cost[i - 1] + abs(A[i - 1] - A[i])
    
    # Return the total cost of travel when visiting each spot, except the last spot
    return cost[:-1]

def main():
    N = int(input())
    A = list(map(int, input().split()))
    cost = get_cost(A, N)
    for i in range(N):
        print(cost[i])

if __name__ == '__main__':
    main()

