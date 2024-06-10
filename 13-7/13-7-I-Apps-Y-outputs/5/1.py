
def get_cost(N, M, X, A):
    # Initialize the cost array with 0s
    cost = [0] * (N + 1)

    # Set the initial cost to 0
    cost[X] = 0

    # Loop through each toll gate
    for i in range(M):
        # Get the current toll gate
        current_toll_gate = A[i]

        # Loop through each square
        for j in range(N + 1):
            # Check if the current square is adjacent to the current toll gate
            if j == current_toll_gate - 1 or j == current_toll_gate + 1:
                # Increment the cost of the current square by 1
                cost[j] += 1

    # Return the minimum cost
    return min(cost)

def main():
    # Read the input
    N, M, X = map(int, input().split())
    A = list(map(int, input().split()))

    # Get the cost
    cost = get_cost(N, M, X, A)

    # Print the cost
    print(cost)

if __name__ == '__main__':
    main()

