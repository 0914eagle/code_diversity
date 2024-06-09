
def get_division(n, c, encounters):
    # Initialize the division as two empty lists
    division = [[], []]
    
    # Sort the encounters by year in ascending order
    encounters.sort(key=lambda x: x[2])
    
    # Iterate through the encounters
    for encounter in encounters:
        # Get the year of the encounter
        year = encounter[2]
        
        # Check if the year is less than or equal to the number of participants divided by 3
        if year <= n // 3:
            # Add the participants to the first list
            division[0].append(encounter[0])
            division[0].append(encounter[1])
        else:
            # Add the participants to the second list
            division[1].append(encounter[0])
            division[1].append(encounter[1])
    
    # Return the division
    return division

def main():
    # Read the number of participants and known encounters
    n, c = map(int, input().split())
    
    # Read the encounters
    encounters = []
    for _ in range(c):
        a, b, y = map(int, input().split())
        encounters.append((a, b, y))
    
    # Get the division
    division = get_division(n, c, encounters)
    
    # Check if the division is possible
    if len(division[0]) <= n // 3 and len(division[1]) <= n // 3:
        # Print the division
        print(division)
    else:
        # Print 'Impossible'
        print('Impossible')

if __name__ == '__main__':
    main()

