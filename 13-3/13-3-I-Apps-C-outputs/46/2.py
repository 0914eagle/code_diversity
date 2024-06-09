
def get_badge_numbers(rooms, locks, start_room, end_room):
    # Initialize a set to store the badge numbers that can pass from the start room to the end room
    badge_numbers = set()

    # Iterate through the locks
    for lock in locks:
        # Extract the information from the lock
        room_a, room_b, lower_bound, upper_bound = lock

        # Check if the lock is between the start and end rooms
        if room_a == start_room and room_b == end_room:
            # Add the badge numbers within the range to the set
            badge_numbers.update(range(lower_bound, upper_bound + 1))

    # Return the number of badge numbers in the set
    return len(badge_numbers)

# Main function
if __name__ == "__main__":
    # Read the input
    rooms, locks, start_room, end_room = map(int, input().split())
    locks = [tuple(map(int, input().split())) for _ in range(locks)]

    # Call the function to get the number of badge numbers that can pass from the start room to the end room
    result = get_badge_numbers(rooms, locks, start_room, end_room)

    # Print the result
    print(result)

