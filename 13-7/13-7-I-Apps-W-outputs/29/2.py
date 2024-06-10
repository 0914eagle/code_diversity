
def get_minimum_sweets(n, t, street):
    # Initialize variables
    k = 0
    time = 0
    houses = 0
    shops = 0
    visited_houses = set()
    visited_shops = set()

    # Iterate through the street
    for i in range(n):
        # If the current section is a house, increment the number of houses and check if it has been visited
        if street[i] == "H":
            houses += 1
            if i not in visited_houses:
                visited_houses.add(i)
                time += 1
        # If the current section is a shop, increment the number of shops and check if it has been visited
        elif street[i] == "S":
            shops += 1
            if i not in visited_shops:
                visited_shops.add(i)
                time += 1
        # If the current section is empty, increment the time by 1
        else:
            time += 1

    # Calculate the minimum number of kilograms of sweets needed
    k = max(houses - len(visited_houses), shops - len(visited_shops))

    # Check if the time is sufficient
    if time <= t:
        return k
    else:
        return -1

def main():
    n, t = map(int, input().split())
    street = input()
    print(get_minimum_sweets(n, t, street))

if __name__ == '__main__':
    main()

