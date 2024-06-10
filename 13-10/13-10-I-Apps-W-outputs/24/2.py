
def get_unique_floor(n, m, memory):
    # Initialize a dictionary to store the number of flats on each floor
    flats_per_floor = {}

    # Loop through each flat in Polycarp's memory
    for k, f in memory:
        # If the floor is already in the dictionary, increment the number of flats on that floor
        if f in flats_per_floor:
            flats_per_floor[f] += 1
        # Otherwise, add the floor to the dictionary with a value of 1
        else:
            flats_per_floor[f] = 1

    # Loop through the dictionary in reverse order (starting from the highest floor)
    for floor, flats in reversed(list(flats_per_floor.items())):
        # If the current floor has an equal number of flats as the total number of flats in Polycarp's memory
        if flats == m:
            # Return the current floor if it is greater than or equal to the flat we are trying to find
            if floor >= n:
                return floor

    # If we reach this point, it is not possible to uniquely restore the floor for the flat
    return -1

def main():
    n, m = map(int, input().split())
    memory = []
    for _ in range(m):
        k, f = map(int, input().split())
        memory.append((k, f))
    print(get_unique_floor(n, m, memory))

if __name__ == '__main__':
    main()

