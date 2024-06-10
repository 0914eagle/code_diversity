
def get_minimum_k(n, t, street):
    # Initialize variables
    k = 0
    time = 0
    current_section = 0
    sections = []

    # Parse the input string
    for i in range(n):
        if street[i] == "H":
            sections.append(("H", i))
        elif street[i] == "S":
            sections.append(("S", i))
        else:
            sections.append(("E", i))

    # Loop through the sections
    while current_section < n:
        section = sections[current_section]
        if section[0] == "H":
            # Give one kilogram of sweets to the inhabitants of the house
            time += 1
            current_section += 1
        elif section[0] == "S":
            # Buy one kilogram of sweets from the shop
            time += 1
            current_section += 1
            k += 1
        else:
            # Move to the next section
            time += 1
            current_section += 1

    # Check if there is enough time to give sweets to all the residents
    if time <= t:
        return k
    else:
        return -1

def main():
    n, t = map(int, input().split())
    street = input()
    print(get_minimum_k(n, t, street))

if __name__ == '__main__':
    main()

