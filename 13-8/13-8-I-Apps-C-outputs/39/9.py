
def solve_council_members(n, residents):
    # Initialize a dictionary to store the number of council members for each party
    party_council_members = {}
    # Initialize a list to store the selected council members
    selected_council_members = []

    # Iterate over the residents
    for resident in residents:
        # Get the party and club names for the current resident
        party, club_names = resident
        # If the party is not in the dictionary, add it with a count of 0
        if party not in party_council_members:
            party_council_members[party] = 0
        # Iterate over the club names
        for club_name in club_names:
            # If the club name is not in the dictionary, add it with a count of 0
            if club_name not in party_council_members:
                party_council_members[club_name] = 0
            # Increment the count for the current party and club
            party_council_members[party] += 1
            party_council_members[club_name] += 1

    # Sort the parties by their count in descending order
    sorted_parties = sorted(party_council_members.items(), key=lambda x: x[1], reverse=True)

    # Iterate over the sorted parties
    for party, count in sorted_parties:
        # If the count is less than or equal to half the number of residents, break the loop
        if count <= n / 2:
            break
        # Add the party to the selected council members
        selected_council_members.append(party)

    # If no council can be formed, return "Impossible"
    if len(selected_council_members) == 0:
        return "Impossible"

    # Initialize a dictionary to store the clubs represented by each council member
    club_representatives = {}

    # Iterate over the selected council members
    for council_member in selected_council_members:
        # If the council member is not in the dictionary, add it with an empty list of clubs
        if council_member not in club_representatives:
            club_representatives[council_member] = []
        # Iterate over the clubs represented by the current council member
        for club in club_representatives[council_member]:
            # If the club is not in the dictionary, add it with a count of 0
            if club not in party_council_members:
                party_council_members[club] = 0
            # Increment the count for the current club
            party_council_members[club] += 1

    # Sort the clubs by their count in descending order
    sorted_clubs = sorted(party_council_members.items(), key=lambda x: x[1], reverse=True)

    # Iterate over the sorted clubs
    for club, count in sorted_clubs:
        # If the count is less than or equal to half the number of residents, break the loop
        if count <= n / 2:
            break
        # Add the club to the selected council members
        selected_council_members.append(club)

    # Return the selected council members in the required format
    return "\n".join([str(member) for member in selected_council_members])

