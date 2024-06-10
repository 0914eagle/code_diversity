
def get_portals(n, portals):
    # Initialize a dictionary to store the number of crosses in each room
    crosses = {1: 1}
    
    # Initialize a variable to store the number of portal moves
    moves = 0
    
    # Start from the first room
    current_room = 1
    
    # Loop until the last room is reached
    while current_room != n + 1:
        # If the ceiling contains an odd number of crosses, use the second portal
        if crosses[current_room] % 2 == 1:
            current_room = portals[current_room - 1]
        # Otherwise, use the first portal
        else:
            current_room += 1
        
        # Increment the number of moves
        moves += 1
        
        # Update the number of crosses in the current room
        crosses[current_room] += 1
    
    # Return the number of portal moves
    return moves % 1000000007

def main():
    n = int(input())
    portals = [int(x) for x in input().split()]
    print(get_portals(n, portals))

if __name__ == '__main__':
    main()

