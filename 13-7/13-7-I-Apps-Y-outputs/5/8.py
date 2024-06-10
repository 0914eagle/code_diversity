
def get_min_cost(n, m, x, a):
    # Initialize the minimum cost array with 0s
    min_cost = [0] * (n + 1)
    # Initialize the previous array with -1s
    prev = [-1] * (n + 1)
    # Loop through each toll gate
    for i in range(m):
        # Get the current toll gate
        curr_toll = a[i]
        # Loop through each square
        for j in range(n + 1):
            # If the current square is the previous square or the current square is the toll gate, skip it
            if j == prev[j] or j == curr_toll:
                continue
            # If the current square is not the previous square or the current square is not the toll gate, check if the minimum cost is greater than the current cost + 1
            if min_cost[j] > min_cost[prev[j]] + 1:
                # If it is, update the minimum cost and the previous square
                min_cost[j] = min_cost[prev[j]] + 1
                prev[j] = prev[prev[j]]
    # Return the minimum cost of reaching the goal
    return min_cost[n]

def main():
    # Read the input
    n, m, x = map(int, input().split())
    a = list(map(int, input().split()))
    # Call the get_min_cost function and print the result
    print(get_min_cost(n, m, x, a))

if __name__ == '__main__':
    main()

