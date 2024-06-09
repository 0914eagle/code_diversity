
def f1(n, residents):
    # Initialize variables
    council_members = []
    club_representatives = {}
    party_members = {}

    # Iterate through each resident
    for resident in residents:
        # Get the resident's information
        name, party, num_clubs, *clubs = resident.split()

        # Add the resident to the party members list
        if party not in party_members:
            party_members[party] = []
        party_members[party].append(name)

        # Add the resident to the club representatives list
        for club in clubs:
            if club not in club_representatives:
                club_representatives[club] = name

    # Iterate through each club
    for club, representative in club_representatives.items():
        # Check if the representative is already in the council
        if representative in council_members:
            continue

        # Add the representative to the council
        council_members.append(representative)

        # Remove the representative from the party members list
        party = party_members[representative]
        party_members[party].remove(representative)

    # Check if the council is valid
    if len(council_members) == n:
        return council_members

    # If the council is not valid, return "Impossible"
    return "Impossible"

def f2(n, residents):
    # Initialize variables
    council_members = []
    club_representatives = {}
    party_members = {}

    # Iterate through each resident
    for resident in residents:
        # Get the resident's information
        name, party, num_clubs, *clubs = resident.split()

        # Add the resident to the party members list
        if party not in party_members:
            party_members[party] = []
        party_members[party].append(name)

        # Add the resident to the club representatives list
        for club in clubs:
            if club not in club_representatives:
                club_representatives[club] = name

    # Iterate through each club
    for club, representative in club_representatives.items():
        # Check if the representative is already in the council
        if representative in council_members:
            continue

        # Add the representative to the council
        council_members.append(representative)

        # Remove the representative from the party members list
        party = party_members[representative]
        party_members[party].remove(representative)

    # Check if the council is valid
    if len(council_members) == n:
        return council_members

    # If the council is not valid, return "Impossible"
    return "Impossible"

if __name__ == '__main__':
    num_test_cases = int(input())
    for i in range(num_test_cases):
        n = int(input())
        residents = []
        for j in range(n):
            residents.append(input())
        council_members = f1(n, residents)
        print(*council_members)
        print()

