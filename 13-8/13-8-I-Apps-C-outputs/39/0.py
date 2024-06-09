
def solve_town_council(residents):
    # Initialize variables
    council_members = []
    clubs = []
    party_members = {}

    # Iterate through each resident
    for resident in residents:
        # Add the resident to the party_members dictionary if they are not already present
        if resident[1] not in party_members:
            party_members[resident[1]] = []
        # Add the resident to the party_members dictionary
        party_members[resident[1]].append(resident[0])
        # Add the resident's clubs to the clubs list if they are not already present
        for club in resident[2:]:
            if club not in clubs:
                clubs.append(club)

    # Iterate through each club
    for club in clubs:
        # Get the number of members in the current club
        num_members = len([resident for resident in residents if club in resident[2:]])
        # Get the number of members in the current club who are from the current party
        num_party_members = len([resident for resident in residents if club in resident[2:] and resident[1] == party])
        # Check if the number of members in the current club who are from the current party is less than or equal to half the number of members in the club
        if num_party_members <= num_members / 2:
            # Add the club to the council_members list
            council_members.append(club)

    # Return the council_members list
    return council_members

