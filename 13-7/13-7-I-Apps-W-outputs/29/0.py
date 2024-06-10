
def solve(n, t, streets):
    # Initialize variables
    k = 0
    time = 0
    houses = 0
    shops = 0
    visited_shops = set()

    # Iterate through the streets
    for i in range(n):
        # If the current street is a house, increment the number of houses and the time
        if streets[i] == "H":
            houses += 1
            time += 1
        # If the current street is a shop, increment the number of shops and the time, and mark the shop as visited
        elif streets[i] == "S":
            shops += 1
            time += 1
            visited_shops.add(i)
        # If the current street is empty, increment the time
        else:
            time += 1

    # Calculate the minimum number of kilograms of sweets needed to give to each house
    min_sweets = houses // t

    # If the minimum number of kilograms of sweets is greater than the number of shops, return -1
    if min_sweets > shops:
        return -1

    # Initialize a variable to keep track of the number of kilograms of sweets needed
    needed_sweets = 0

    # Iterate through the streets again
    for i in range(n):
        # If the current street is a house and it has not been visited yet, increment the number of kilograms of sweets needed
        if streets[i] == "H" and i not in visited_shops:
            needed_sweets += 1

    # Return the minimum number of kilograms of sweets needed to give to each house
    return needed_sweets

def main():
    n, t = map(int, input().split())
    streets = input()
    print(solve(n, t, streets))

if __name__ == '__main__':
    main()

