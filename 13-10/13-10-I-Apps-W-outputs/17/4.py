
def get_min_distance(n, k, rooms):
    # Initialize variables
    min_distance = float('inf')
    free_rooms = []

    # Loop through the string of rooms
    for i in range(n):
        # If the room is free, add it to the list of free rooms
        if rooms[i] == '0':
            free_rooms.append(i)

            # If there are k + 1 free rooms, we can book them all
            if len(free_rooms) == k + 1:
                # Calculate the minimum distance between Farmer John's room and his farthest cow
                min_distance = min(abs(free_rooms[0] - free_rooms[k]), abs(free_rooms[k] - free_rooms[0]))

                # Break out of the loop
                break

    # Return the minimum distance
    return min_distance

def main():
    # Read the input
    n, k = map(int, input().split())
    rooms = input()

    # Call the get_min_distance function
    min_distance = get_min_distance(n, k, rooms)

    # Print the result
    print(min_distance)

if __name__ == '__main__':
    main()

