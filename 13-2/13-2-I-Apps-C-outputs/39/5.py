
def get_council_members(n, residents):
    # Initialize a dictionary to store the council members and the clubs they represent
    council_members = {}
    
    # Iterate through the residents and their clubs
    for resident in residents:
        # Get the resident's name and the clubs they belong to
        name, party, num_clubs, *clubs = resident.split()
        
        # Check if the resident is already in the council
        if name not in council_members:
            # If not, add them to the council and assign them a club to represent
            council_members[name] = clubs[0]
        else:
            # If the resident is already in the council, remove them from the club they represent
            club_to_remove = council_members[name]
            clubs.remove(club_to_remove)
            
            # Add the resident to the council and assign them a new club to represent
            council_members[name] = clubs[0]
    
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
        print()

if __name__ == '__main__':
    main()

