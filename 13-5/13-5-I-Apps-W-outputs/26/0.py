
def get_min_cost(n, c, a):
    # Initialize a list to store the minimum cost of setting traps in each room
    min_cost = [float('inf') for _ in range(n + 1)]
    # Initialize a list to store the previous room number of each room
    prev_room = [0 for _ in range(n + 1)]
    
    # Set the minimum cost of setting a trap in room 1 to 0
    min_cost[1] = 0
    
    # Loop through each room
    for i in range(2, n + 1):
        # Loop through each previous room
        for j in range(1, i):
            # If the cost of setting a trap in room j is less than the minimum cost of setting a trap in room i
            if min_cost[j] + c[j] < min_cost[i]:
                # Update the minimum cost of setting a trap in room i
                min_cost[i] = min_cost[j] + c[j]
                # Update the previous room number of room i
                prev_room[i] = j
    
    # Initialize a list to store the rooms where traps need to be set
    rooms_to_set = []
    
    # Start from the last room
    i = n
    # Loop until the previous room is 0
    while prev_room[i] != 0:
        # Add the current room to the list of rooms where traps need to be set
        rooms_to_set.append(i)
        # Move to the previous room
        i = prev_room[i]
    
    # Add the first room to the list of rooms where traps need to be set
    rooms_to_set.append(1)
    
    # Return the minimum cost of setting traps in all the rooms where traps need to be set
    return sum(c[i - 1] for i in rooms_to_set)

def main():
    n, c, a = map(int, input().split())
    c = list(map(int, input().split()))
    a = list(map(int, input().split()))
    print(get_min_cost(n, c, a))

if __name__ == '__main__':
    main()

