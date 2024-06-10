
def get_number_of_portals(n, portals):
    # Initialize variables
    number_of_portals = 0
    current_room = 1
    visited_rooms = set()

    # Loop through each room
    for i in range(n):
        # If the current room has not been visited before
        if current_room not in visited_rooms:
            # Add the current room to the set of visited rooms
            visited_rooms.add(current_room)
            # If the ceiling contains an odd number of crosses
            if len(visited_rooms) % 2 == 1:
                # Use the second portal (leads to room p_i)
                current_room = portals[current_room - 1]
            else:
                # Use the first portal (leads to room i + 1)
                current_room += 1
        # If the current room has been visited before
        else:
            # Add one to the number of portals
            number_of_portals += 1
            # Break out of the loop
            break

    # Return the number of portals
    return number_of_portals

def main():
    # Read the input
    n = int(input())
    portals = list(map(int, input().split()))

    # Call the function to get the number of portals
    number_of_portals = get_number_of_portals(n, portals)

    # Print the output
    print(number_of_portals % 1000000007)

if __name__ == '__main__':
    main()

