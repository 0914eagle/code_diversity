
def get_floor(n, memory):
    # Initialize a dictionary to store the number of flats on each floor
    floors = {}

    # Iterate over the memory and increment the count of flats on each floor
    for flat, floor in memory:
        floors[floor] = floors.get(floor, 0) + 1

    # Find the floor with an equal number of flats before and after it
    for floor, count in floors.items():
        if count == floors.get(floor + 1, 0):
            return floor

    # If no matching floor is found, return -1
    return -1

def main():
    n, m = map(int, input().split())
    memory = [tuple(map(int, input().split())) for _ in range(m)]
    print(get_floor(n, memory))

if __name__ == '__main__':
    main()

