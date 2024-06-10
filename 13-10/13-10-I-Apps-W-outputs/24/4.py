
def get_floor(n, memory):
    # Initialize a dictionary to store the number of flats on each floor
    floors = {}
    
    # Iterate over the memory of Polycarp
    for flat, floor in memory:
        # If the floor is not in the dictionary, add it with a value of 1
        if floor not in floors:
            floors[floor] = 1
        # If the floor is already in the dictionary, increment its value by 1
        else:
            floors[floor] += 1
    
    # Initialize a variable to store the number of flats on each floor
    num_flats = 0
    
    # Iterate over the dictionary in reverse order (from highest floor to lowest floor)
    for floor, count in reversed(list(floors.items())):
        # If the number of flats on this floor is equal to the number of flats on the previous floor, return the current floor
        if count == num_flats:
            return floor
        # Otherwise, update the number of flats on this floor and continue iterating
        num_flats = count
    
    # If we reach this point, it means that the flat is on the lowest floor, return -1
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

