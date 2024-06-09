
def get_min_cost(n, c_list, a_list):
    # Initialize a list to store the minimum cost for each room
    min_cost = [float('inf') for _ in range(n + 1)]
    # Initialize a list to store the previous room for each room
    prev_room = [0 for _ in range(n + 1)]
    
    # Set the minimum cost for room 1 to 0
    min_cost[1] = 0
    
    # Loop through each room
    for i in range(1, n + 1):
        # Loop through each possible previous room
        for j in range(1, n + 1):
            # If the cost of setting a trap in room i is less than the minimum cost of room j
            if c_list[i - 1] < min_cost[j]:
                # Update the minimum cost and previous room for room i
                min_cost[i] = c_list[i - 1]
                prev_room[i] = j
    
    # Initialize a list to store the rooms that need to be trapped
    trapped_rooms = []
    
    # Start from the last room
    current_room = n
    
    # Loop until the mouse is trapped
    while current_room != 0:
        # Add the current room to the list of trapped rooms
        trapped_rooms.append(current_room)
        # Move to the previous room
        current_room = prev_room[current_room]
    
    # Return the total cost of trapping all the rooms
    return sum(c_list[i - 1] for i in trapped_rooms)

def main():
    n = int(input())
    c_list = [int(x) for x in input().split()]
    a_list = [int(x) for x in input().split()]
    print(get_min_cost(n, c_list, a_list))

if __name__ == '__main__':
    main()

