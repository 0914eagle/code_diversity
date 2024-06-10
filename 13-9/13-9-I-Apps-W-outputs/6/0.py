
def get_cables(n, x, c):
    # Initialize variables
    cables = []
    current_city = 0
    current_cost = 0
    
    # Iterate through the cities
    for i in range(n):
        # If the current city is of the same type as the previous city, add the distance to the current cost
        if c[current_city] == c[i]:
            current_cost += abs(x[i] - x[current_city])
        # If the current city is of a different type, add the current cost to the list of cables and reset the current cost
        else:
            cables.append(current_cost)
            current_cost = 0
        # Update the current city and city type
        current_city = i
    
    # Add the last cost to the list of cables
    cables.append(current_cost)
    
    return cables

def get_min_cost(n, x, c):
    # Get the list of cables
    cables = get_cables(n, x, c)
    
    # Initialize variables
    min_cost = 0
    byteland_cables = 0
    berland_cables = 0
    
    # Iterate through the cables
    for i in range(n - 1):
        # If the current city is of the same type as the next city, add the cost of the current cable to the min cost
        if c[i] == c[i + 1]:
            min_cost += cables[i]
        # If the current city is of a different type, add the cost of the current cable to the respective total cost
        else:
            if c[i] == 'B':
                byteland_cables += cables[i]
            else:
                berland_cables += cables[i]
    
    # Add the cost of the last cable to the respective total cost
    if c[n - 1] == 'B':
        byteland_cables += cables[n - 1]
    else:
        berland_cables += cables[n - 1]
    
    # Return the minimum total cost
    return min_cost + min(byteland_cables, berland_cables)

def main():
    n = int(input())
    x = []
    c = []
    for i in range(n):
        xi, ci = input().split()
        x.append(int(xi))
        c.append(ci)
    print(get_min_cost(n, x, c))

if __name__ == '__main__':
    main()

