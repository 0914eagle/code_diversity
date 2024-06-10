
def get_floor(n, m, memory):
    # Initialize a dictionary to store the number of flats on each floor
    floors = {}

    # Iterate over the memory and update the dictionary
    for k, f in memory:
        if f not in floors:
            floors[f] = 1
        else:
            floors[f] += 1

    # Find the floor with the closest match to the number of flats on each floor
    min_diff = float('inf')
    closest_floor = -1
    for f, count in floors.items():
        diff = abs(count - n)
        if diff < min_diff:
            min_diff = diff
            closest_floor = f

    # If the closest floor has an exact match, return it
    if min_diff == 0:
        return closest_floor

    # Otherwise, return -1
    return -1

def main():
    n, m = map(int, input().split())
    memory = [tuple(map(int, input().split())) for _ in range(m)]
    print(get_floor(n, m, memory))

if __name__ == '__main__':
    main()

