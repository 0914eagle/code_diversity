
def get_floor(n, memory):
    # Initialize variables
    floors = {}
    flats_per_floor = 0
    current_floor = 1
    total_flats = 0

    # Iterate over the memory
    for flat, floor in memory:
        # Check if the flat is on a new floor
        if floor != current_floor:
            # Update the current floor and the number of flats per floor
            current_floor = floor
            flats_per_floor = total_flats

        # Update the total number of flats
        total_flats += 1

        # Add the flat to the dictionary with its floor
        floors[flat] = floor

    # Check if the flat is in the dictionary
    if n in floors:
        # Return the floor of the flat
        return floors[n]
    else:
        # Return -1 if the flat is not in the dictionary
        return -1

def main():
    # Read the input
    n, m = map(int, input().split())
    memory = []
    for _ in range(m):
        k, f = map(int, input().split())
        memory.append((k, f))

    # Call the function to get the floor
    result = get_floor(n, memory)

    # Print the result
    print(result)

if __name__ == '__main__':
    main()

