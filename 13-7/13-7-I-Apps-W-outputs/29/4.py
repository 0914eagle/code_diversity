
def get_min_sweets(n, t, street):
    # Initialize variables
    sweets_needed = 0
    time_spent = 0
    current_section = 0
    sections_visited = set()
    sections_with_houses = [i for i, char in enumerate(street) if char == "H"]
    sections_with_shops = [i for i, char in enumerate(street) if char == "S"]

    # Loop through the street
    while time_spent <= t and current_section < n:
        # If the current section is a house section
        if current_section in sections_with_houses:
            # Give a kilogram of sweets to the inhabitants of the house
            sweets_needed += 1
            # Move to the next section
            current_section += 1
        # If the current section is a shop section
        elif current_section in sections_with_shops:
            # Buy a kilogram of sweets from the shop
            sweets_needed += 1
            # Move to the next section
            current_section += 1
        # If the current section is an empty section
        else:
            # Move to the next section
            current_section += 1
        # Add the time spent on the current section to the total time spent
        time_spent += 1

    # Return the minimum number of kilograms of sweets needed
    return sweets_needed

def main():
    n, t = map(int, input().split())
    street = input()
    print(get_min_sweets(n, t, street))

if __name__ == '__main__':
    main()

