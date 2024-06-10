
def get_floor(n, m, floors):
    # Initialize a set to store the floors where flats are located
    flat_floors = set()
    
    # Iterate over the flats in Polycarp's memory
    for flat, floor in floors:
        # If the flat is the n-th flat, return its floor
        if flat == n:
            return floor
        # Otherwise, add the floor to the set of flat floors
        else:
            flat_floors.add(floor)
    
    # If the set of flat floors has only one element, return that element
    if len(flat_floors) == 1:
        return flat_floors.pop()
    # Otherwise, return -1
    else:
        return -1

def main():
    n, m = map(int, input().split())
    floors = []
    for i in range(m):
        flat, floor = map(int, input().split())
        floors.append((flat, floor))
    print(get_floor(n, m, floors))

if __name__ == '__main__':
    main()

