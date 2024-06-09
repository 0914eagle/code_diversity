
def get_council_members(n, residents):
    # Initialize a dictionary to store the council members and the clubs they represent
    council_members = {}
    
    # Iterate through the residents and their clubs
    for resident in residents:
        # Get the resident's name and the clubs they belong to
        name, party, num_clubs, *clubs = resident.split()
        
        # Check if the resident is already in the council
        if name in council_members:
            # If the resident is already in the council, skip them
            continue
        
        # Check if the resident belongs to more than one club
        if num_clubs > 1:
            # If the resident belongs to more than one club, assign them to the club with the least number of members
            club = min(clubs, key=lambda c: len(council_members.get(c, [])))
        else:
            # If the resident belongs to only one club, assign them to that club
            club = clubs[0]
        
        # Add the resident to the council and the club they represent
        council_members[name] = club
    
    # Return the council members and the clubs they represent
    return council_members

def main():
    # Read the number of test cases
    num_test_cases = int(input())
    
    # Iterate through the test cases
    for _ in range(num_test_cases):
        # Read the number of residents
        n = int(input())
        
        # Read the residents and their clubs
        residents = [input() for _ in range(n)]
        
        # Get the council members and the clubs they represent
        council_members = get_council_members(n, residents)
        
        # Print the council members and the clubs they represent
        for name, club in council_members.items():
            print(name, club)
        
        # Print a blank line to separate the test cases
        print()

if __name__ == '__main__':
    main()

