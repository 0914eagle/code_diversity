
def get_min_cost(n, c, a):
    # Initialize a list to store the minimum cost of setting traps in each room
    min_cost = [float('inf') for _ in range(n + 1)]
    # Initialize a list to store the previous room of each room
    prev_room = [0 for _ in range(n + 1)]
    
    # Set the minimum cost of setting a trap in room 1 to 0
    min_cost[1] = 0
    
    # Loop through each room
    for i in range(2, n + 1):
        # Loop through each previous room
        for j in range(1, i):
            # If the minimum cost of setting a trap in the previous room plus the cost of setting a trap in the current room is less than the minimum cost of setting a trap in the current room, update the minimum cost and the previous room
            if min_cost[j] + c[i - 1] < min_cost[i]:
                min_cost[i] = min_cost[j] + c[i - 1]
                prev_room[i] = j
    
    # Initialize a list to store the path of the mouse
    path = []
    
    # Start from the last room
    curr_room = n
    
    # Loop until the mouse reaches room 1
    while curr_room != 1:
        # Add the current room to the path
        path.append(curr_room)
        # Move to the previous room
        curr_room = prev_room[curr_room]
    
    # Add room 1 to the path
    path.append(1)
    
    # Return the minimum cost of setting traps in the rooms in the path
    return sum(c[i - 1] for i in path)

def main():
    n = int(input())
    c = list(map(int, input().split()))
    a = list(map(int, input().split()))
    print(get_min_cost(n, c, a))

if __name__ == '__main__':
    main()

