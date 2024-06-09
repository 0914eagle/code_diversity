
def get_min_cost(n, c, a):
    # Initialize a list to store the minimum cost of setting traps in each room
    min_cost = [float('inf') for _ in range(n + 1)]
    # Set the minimum cost of setting a trap in the last room to 0
    min_cost[n] = 0
    # Loop through the rooms in reverse order
    for i in range(n - 1, -1, -1):
        # If the mouse can reach the current room from the next room
        if a[i] > i:
            # Update the minimum cost of setting a trap in the current room
            min_cost[i] = min(min_cost[i], c[i] + min_cost[a[i]])
        # If the mouse can reach the current room from the previous room
        if a[i - 1] < i:
            # Update the minimum cost of setting a trap in the current room
            min_cost[i] = min(min_cost[i], c[i] + min_cost[a[i - 1]])
    # Return the minimum cost of setting traps in all rooms
    return min_cost[0]

def main():
    n = int(input())
    c = list(map(int, input().split()))
    a = list(map(int, input().split()))
    print(get_min_cost(n, c, a))

if __name__ == '__main__':
    main()

