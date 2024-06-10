
def get_floor_of_flat(n, memory):
    # Initialize a dictionary to store the number of flats on each floor
    floors = {}

    # Loop through the memory and update the dictionary
    for flat, floor in memory:
        if floor not in floors:
            floors[floor] = 1
        else:
            floors[floor] += 1

    # Find the floor with the right number of flats
    for floor, num_flats in floors.items():
        if num_flats == n:
            return floor

    # If we reach this point, it means we couldn't find a floor with the right number of flats
    return -1

def main():
    n, m = map(int, input().split())
    memory = []
    for _ in range(m):
        flat, floor = map(int, input().split())
        memory.append((flat, floor))
    print(get_floor_of_flat(n, memory))

if __name__ == '__main__':
    main()

