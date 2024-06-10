
def solve(n, t, road):
    # Initialize variables
    k = 0
    time = 0
    houses = 0
    shops = 0
    visited = set()
    queue = []

    # Add the first section of the road to the queue
    queue.append((0, 0))

    # Loop through the queue
    while queue:
        # Get the current section and the time it takes to get there
        section, time = queue.pop(0)

        # If the section is a house, give sweets to the inhabitants and update the number of houses visited
        if road[section] == "H":
            houses += 1
            time += 1

        # If the section is a shop, buy a kilogram of sweets and update the number of shops visited
        elif road[section] == "S":
            shops += 1
            time += 1

        # If the section is not a house or a shop, move to the next section
        else:
            time += 1

        # If the family has given sweets to all the inhabitants of the houses, break the loop
        if houses == n:
            break

        # If the family has visited all the sections, break the loop
        if time == t:
            break

        # Add the next sections to the queue
        for i in range(section+1, len(road)):
            if road[i] != "." and i not in visited:
                queue.append((i, time+1))
                visited.add(i)

    # Calculate the minimum number of kilograms of sweets needed
    k = shops + (n - houses)

    # Return the result
    return k

def main():
    # Read the input
    n, t = map(int, input().split())
    road = list(input())

    # Solve the problem
    result = solve(n, t, road)

    # Print the result
    print(result)

if __name__ == '__main__':
    main()

