
def get_min_cost(n, c, a):
    # Initialize a list to store the minimum cost of setting traps in each room
    min_cost = [float('inf') for i in range(n + 1)]
    # Initialize a list to store the previous room of each room
    prev = [0 for i in range(n + 1)]
    
    # Set the minimum cost of setting a trap in room 1 to 0
    min_cost[1] = 0
    
    # Loop through each room
    for i in range(2, n + 1):
        # Loop through each previous room
        for j in range(1, i):
            # If the minimum cost of setting a trap in the previous room plus the cost of setting a trap in the current room is less than the minimum cost of setting a trap in the current room, update the minimum cost and the previous room
            if min_cost[j] + c[i - 1] < min_cost[i]:
                min_cost[i] = min_cost[j] + c[i - 1]
                prev[i] = j
    
    # Initialize a list to store the rooms where traps need to be set
    rooms = []
    
    # Start from the last room
    i = n
    
    # Loop until the first room is reached
    while i > 0:
        # If the minimum cost of setting a trap in the current room is less than the minimum cost of setting a trap in the previous room, update the minimum cost and the previous room
        if min_cost[i] < min_cost[prev[i]]:
            min_cost[prev[i]] = min_cost[i]
            prev[prev[i]] = i
        # Add the current room to the list of rooms where traps need to be set
        rooms.append(i)
        # Move to the previous room
        i = prev[i]
    
    # Return the minimum cost of setting traps in all the rooms where traps need to be set
    return sum(c[i - 1] for i in rooms)

def main():
    n = int(input())
    c = list(map(int, input().split()))
    a = list(map(int, input().split()))
    print(get_min_cost(n, c, a))

if __name__ == '__main__':
    main()

