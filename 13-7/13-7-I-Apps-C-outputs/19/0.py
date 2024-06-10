
def get_division(n, c, encounters):
    # Sort the encounters by the year of the first encounter
    encounters.sort(key=lambda x: x[2])
    
    # Initialize the division as an empty list
    division = []
    
    # Iterate through the encounters and add them to the division
    for encounter in encounters:
        division.append(encounter[0])
        division.append(encounter[1])
    
    # Check if the division is valid
    if len(set(division)) == n:
        return division
    else:
        return "Impossible"

def main():
    n, c = map(int, input().split())
    encounters = []
    for _ in range(c):
        a, b, y = map(int, input().split())
        encounters.append((a, b, y))
    print(get_division(n, c, encounters))

if __name__ == '__main__':
    main()

