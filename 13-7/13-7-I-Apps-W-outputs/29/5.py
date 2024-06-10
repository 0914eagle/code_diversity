
def get_min_sweets(n, t, street):
    # Initialize variables
    k = 0
    time = 0
    houses = 0
    shops = 0
    sweets = 0

    # Iterate through the street
    for i in range(n):
        # Check if the current segment is a house
        if street[i] == "H":
            houses += 1
        # Check if the current segment is a shop
        elif street[i] == "S":
            shops += 1
        # Check if the current segment is empty
        elif street[i] == ".":
            pass

    # Calculate the minimum number of sweets needed
    k = houses - shops

    # Return the minimum number of sweets needed
    return k

def main():
    # Read the input
    n, t = map(int, input().split())
    street = input()

    # Call the function to get the minimum number of sweets needed
    k = get_min_sweets(n, t, street)

    # Print the result
    print(k)

if __name__ == '__main__':
    main()

