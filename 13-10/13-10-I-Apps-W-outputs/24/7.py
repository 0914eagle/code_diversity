
def get_floor(n, memory):
    # Initialize a dictionary to store the number of flats on each floor
    floor_count = {}
    # Iterate over the memory to count the number of flats on each floor
    for flat, floor in memory:
        if floor not in floor_count:
            floor_count[floor] = 1
        else:
            floor_count[floor] += 1
    # Find the floor with the highest count that is less than or equal to n
    for floor in sorted(floor_count, reverse=True):
        if floor_count[floor] <= n:
            return floor
    # If we reach this point, it means that we could not find a floor with a count less than or equal to n
    return -1

def main():
    n, m = map(int, input().split())
    memory = []
    for _ in range(m):
        flat, floor = map(int, input().split())
        memory.append((flat, floor))
    print(get_floor(n, memory))

if __name__ == '__main__':
    main()

