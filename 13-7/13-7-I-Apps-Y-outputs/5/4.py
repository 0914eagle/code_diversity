
def get_cost(n, m, x, a):
    # Initialize the cost array with 0s
    cost = [0] * (n + 1)

    # Loop through each toll gate
    for i in range(m):
        # Get the current toll gate
        current_toll = a[i]

        # Loop through each square
        for j in range(n + 1):
            # If the current square is the toll gate or the goal square, skip it
            if j == current_toll or j == 0 or j == n:
                continue

            # If the current square is not the toll gate or the goal square, update the cost
            cost[j] += 1

    # Return the minimum cost
    return min(cost)

def main():
    # Read the input
    n, m, x = map(int, input().split())
    a = list(map(int, input().split()))

    # Get the cost
    cost = get_cost(n, m, x, a)

    # Print the cost
    print(cost)

if __name__ == '__main__':
    main()

