
def get_floor(n, m, memory):
    # Initialize a dictionary to store the number of flats on each floor
    num_flats_on_each_floor = {}
    
    # Loop through the memory and update the dictionary
    for k, f in memory:
        if f not in num_flats_on_each_floor:
            num_flats_on_each_floor[f] = 1
        else:
            num_flats_on_each_floor[f] += 1
    
    # Find the floor with the right number of flats
    for f, num_flats in num_flats_on_each_floor.items():
        if num_flats == n:
            return f
    
    # If we reach this point, it means we couldn't find a floor with the right number of flats
    return -1

def main():
    n, m = map(int, input().split())
    memory = []
    for _ in range(m):
        k, f = map(int, input().split())
        memory.append((k, f))
    print(get_floor(n, m, memory))

if __name__ == '__main__':
    main()

