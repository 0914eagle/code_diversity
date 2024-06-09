
def solve_problem(residents, parties, clubs, council_size):
    # Initialize the dictionary to store the club members
    club_members = {}
    for club in clubs:
        club_members[club] = None

    # Iterate through the residents and assign them to clubs
    for resident in residents:
        # Check if the resident is already assigned to a club
        if club_members[resident[2]] is not None:
            # If the resident is already assigned, skip them
            continue
        # Assign the resident to the club they belong to
        club_members[resident[2]] = resident[0]

    # Initialize the list to store the council members
    council = []
    # Iterate through the clubs and assign them a member
    for club in clubs:
        # Check if the club has a member already
        if club_members[club] is not None:
            # If the club has a member, add them to the council
            council.append((club_members[club], club))
        else:
            # If the club does not have a member, assign a resident to it
            for resident in residents:
                if resident[2] == club:
                    # Assign the resident to the club
                    club_members[club] = resident[0]
                    # Add them to the council
                    council.append((resident[0], club))
                    break

    # Check if the council size is valid
    if len(council) > council_size:
        return "Impossible"

    # Return the council members
    return council

