
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
            # If the minimum cost of setting a trap in the previous room plus the cost of setting a trap in the current room is less than the minimum cost of setting a trap in the current room, update the minimum cost and the previous room number
            if min_cost[j] + c[i - 1] < min_cost[i]:
                min_cost[i] = min_cost[j] + c[i - 1]
                prev_room[i] = j
    
    # Initialize a list to store the rooms where traps need to be set
    trap_rooms = []
    
    # Start from the last room
    curr_room = n
    
    # Loop until the previous room is 0
    while prev_room[curr_room] != 0:
        # Add the current room to the list of rooms where traps need to be set
        trap_rooms.append(curr_room)
        # Set the current room to the previous room
        curr_room = prev_room[curr_room]
    
    # Return the minimum cost of setting traps in the rooms where traps need to be set
    return sum(c[i - 1] for i in trap_rooms)

def main():
    n, c, a = map(int, input().split())
    print(get_min_cost(n, c, a))

if __name__ == '__main__':
    main()

