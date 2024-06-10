
def get_minimum_sweets(n, t, street):
    # Initialize variables
    houses = 0
    shops = 0
    sweets = 0
    time = 0

    # Iterate through the street
    for i in range(n):
        if street[i] == "H":
            houses += 1
        elif street[i] == "S":
            shops += 1

    # Calculate the minimum number of sweets needed
    min_sweets = houses - shops

    # Check if the minimum number of sweets is enough
    if min_sweets <= t:
        return min_sweets
    else:
        return -1

def main():
    n, t = map(int, input().split())
    street = input()
    print(get_minimum_sweets(n, t, street))

if __name__ == '__main__':
    main()

