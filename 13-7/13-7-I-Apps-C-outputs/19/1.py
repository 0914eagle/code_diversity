
def get_possible_year(n, c, encounters):
    # Sort the encounters by year in ascending order
    encounters.sort(key=lambda x: x[2])
    
    # Initialize variables
    year = 1948
    first_part = set()
    second_part = set()
    
    # Iterate through the encounters
    for encounter in encounters:
        a, b, y = encounter
        
        # If the year is before the current year, add the pair to the first part
        if y < year:
            first_part.add(a)
            first_part.add(b)
        # If the year is after the current year, add the pair to the second part
        else:
            second_part.add(a)
            second_part.add(b)
    
    # Check if it is possible to divide the participants into two parts
    if len(first_part) + len(second_part) <= 2 * n / 3:
        return year
    
    # If it is not possible, return 'Impossible'
    return 'Impossible'

def main():
    n, c = map(int, input().split())
    encounters = []
    for _ in range(c):
        a, b, y = map(int, input().split())
        encounters.append((a, b, y))
    print(get_possible_year(n, c, encounters))

if __name__ == '__main__':
    main()

