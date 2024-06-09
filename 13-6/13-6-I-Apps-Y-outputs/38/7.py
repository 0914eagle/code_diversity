
def get_cost(A, N):
    # Calculate the total cost of travel when visiting each spot
    total_cost = [0] * (N + 1)
    for i in range(1, N + 1):
        total_cost[i] = total_cost[i - 1] + abs(A[i - 1] - A[i])
    
    # Return the total cost of travel when visiting each spot, excluding the ith spot
    return [total_cost[i - 1] + total_cost[N] - total_cost[i] for i in range(1, N + 1)]

def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(*get_cost(A, N), sep='\n')

if __name__ == '__main__':
    main()

