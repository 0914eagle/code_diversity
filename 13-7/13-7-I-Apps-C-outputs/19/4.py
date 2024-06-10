
def get_division(n, c, encounters):
    # Sort the encounters by year in ascending order
    encounters.sort(key=lambda x: x[2])
    
    # Initialize the division with the first encounter
    division = [encounters[0]]
    
    # Iterate through the remaining encounters
    for i in range(1, c):
        # If the current encounter is compatible with the division, add it to the division
        if is_compatible(division, encounters[i]):
            division.append(encounters[i])
        # Otherwise, create a new division and add the current encounter to it
        else:
            division = [encounters[i]]
    
    # Return the division
    return division

def is_compatible(division, encounter):
    # If the encounter is not between two people already in the division, return True
    if encounter[0] not in division and encounter[1] not in division:
        return True
    # If the encounter is between two people already in the division, return False
    else:
        return False

def get_year(division):
    # Get the earliest year in the division
    year = min(division, key=lambda x: x[2])[2]
    # Return the year
    return year

def main():
    # Read the input
    n, c = map(int, input().split())
    encounters = []
    for i in range(c):
        a, b, y = map(int, input().split())
        encounters.append((a, b, y))
    
    # Get the division
    division = get_division(n, c, encounters)
    
    # Get the year
    year = get_year(division)
    
    # Print the output
    print(year)

if __name__ == '__main__':
    main()

