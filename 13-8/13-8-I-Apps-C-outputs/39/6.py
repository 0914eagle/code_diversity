
def solve_council_members(residents):
    # Initialize variables
    council_members = []
    club_representatives = {}
    party_members = {}

    # Iterate through each resident
    for resident in residents:
        # Get the resident's information
        name, party, num_clubs, *clubs = resident

        # If the resident is not already a council member
        if name not in council_members:
            # Add the resident to the council members list
            council_members.append(name)

            # Iterate through each club the resident belongs to
            for club in clubs:
                # If the club does not already have a representative
                if club not in club_representatives:
                    # Add the resident as the representative for the club
                    club_representatives[club] = name

                    # Add the resident to the party members list
                    if party not in party_members:
                        party_members[party] = [name]
                    else:
                        party_members[party].append(name)

    # Check if the number of council members for any party exceeds half the number of council members
    for party, members in party_members.items():
        if len(members) > len(council_members) // 2:
            return "Impossible"

    # Return the council members and the clubs they represent
    return "\n".join([f"{member} {club_representatives[club]}" for member in council_members for club in club_representatives if club_representatives[club] == member])

