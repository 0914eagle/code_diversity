
def find_number_of_portals(n, portals):
    # Initialize variables
    current_room = 1
    total_portals = 0
    visited_rooms = set()
    
    # Loop through each room
    for i in range(n):
        # If the current room has not been visited before
        if current_room not in visited_rooms:
            # Add the current room to the set of visited rooms
            visited_rooms.add(current_room)
            # If the number of crosses on the ceiling is odd
            if len(visited_rooms) % 2 == 1:
                # Use the first portal
                current_room = 1
            else:
                # Use the second portal
                current_room = portals[i-1]
            # Increment the total number of portals used
            total_portals += 1
    
    # Return the total number of portals used
    return total_portals % 1000000007

def main():
    n = int(input())
    portals = list(map(int, input().split()))
    print(find_number_of_portals(n, portals))

if __name__ == '__main__':
    main()

