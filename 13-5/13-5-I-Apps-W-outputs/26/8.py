
def get_min_cost(n, c, a):
    # Initialize a list to store the minimum cost for each room
    min_cost = [float('inf') for _ in range(n + 1)]
    # Initialize a list to store the previous room for each room
    prev = [0 for _ in range(n + 1)]
    # Set the minimum cost for room 1 to 0
    min_cost[1] = 0
    # Loop through each room
    for i in range(1, n + 1):
        # Loop through each possible previous room
        for j in range(1, n + 1):
            # If the current room is reachable from the previous room
            if a[i - 1] == j:
                # Calculate the minimum cost for the current room
                min_cost[i] = min(min_cost[i], min_cost[j] + c[i - 1])
                # Set the previous room for the current room
                prev[i] = j
    # Return the minimum cost for the last room
    return min_cost[-1]

def main():
    n = int(input())
    c = list(map(int, input().split()))
    a = list(map(int, input().split()))
    print(get_min_cost(n, c, a))

if __name__ == '__main__':
    main()

