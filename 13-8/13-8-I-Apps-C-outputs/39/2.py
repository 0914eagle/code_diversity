
def solve_town_council(n, residents):
    # Initialize variables
    council_members = []
    clubs = []
    party_members = {}

    # Iterate through each resident
    for resident in residents:
        # Get the resident's information
        name, party, num_clubs, *club_names = resident.split()

        # Add the resident to the party's list of members
        if party not in party_members:
            party_members[party] = []
        party_members[party].append(name)

        # Add the resident's clubs to the list of clubs
        for club_name in club_names:
            clubs.append(club_name)

    # Sort the clubs and party members
    clubs = sorted(clubs)
    party_members = {k: sorted(v) for k, v in party_members.items()}

    # Iterate through each club
    for club in clubs:
        # Get the club's representatives
        representatives = party_members[club]

        # Add the representatives to the council
        for representative in representatives:
            council_members.append(representative)

    return council_members

