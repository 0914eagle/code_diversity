
def get_min_sweets(n, t, street):
    # Initialize variables
    k = 0
    time = 0
    houses = 0
    shops = 0
    visited_houses = set()
    visited_shops = set()
    
    # Iterate through the street
    for i in range(n):
        # Check if the current segment is a house
        if street[i] == "H":
            # Increment the number of houses
            houses += 1
            # Check if the house has already been visited
            if i not in visited_houses:
                # Increment the time and add the house to the visited set
                time += 1
                visited_houses.add(i)
        # Check if the current segment is a shop
        elif street[i] == "S":
            # Increment the number of shops
            shops += 1
            # Check if the shop has already been visited
            if i not in visited_shops:
                # Increment the time and add the shop to the visited set
                time += 1
                visited_shops.add(i)
    
    # Calculate the minimum number of sweets needed
    k = houses - shops
    
    # Check if the time is sufficient
    if time <= t:
        return k
    else:
        return -1

def main():
    n, t = map(int, input().split())
    street = input()
    print(get_min_sweets(n, t, street))

if __name__ == '__main__':
    main()

