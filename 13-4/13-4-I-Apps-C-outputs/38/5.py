
def solve(n, residents):
    # Initialize variables
    council_members = []
    club_representatives = {}
    impossible = False

    # Iterate through each resident
    for resident in residents:
        # Get the resident's information
        name, party, num_clubs, *clubs = resident.split()

        # Check if the resident is already a council member
        if name in council_members:
            continue

        # Check if the resident is already a club representative
        if name in club_representatives:
            continue

        # Check if the resident belongs to any clubs
        if num_clubs == 0:
            continue

        # Check if the resident belongs to more than one club
        if num_clubs > 1:
            # Check if the resident is already a club representative
            if name in club_representatives:
                # The resident is already a club representative, so they cannot be a council member
                impossible = True
                break
            else:
                # The resident is not a club representative, so they can be a council member
                council_members.append(name)
                continue

        # The resident belongs to only one club
        club = clubs[0]

        # Check if the club already has a representative
        if club in club_representatives:
            # The club already has a representative, so the resident cannot be a council member
            impossible = True
            break
        else:
            # The club does not have a representative, so the resident can be a council member and a club representative
            council_members.append(name)
            club_representatives[club] = name

    # Check if the council can be formed
    if impossible:
        return "Impossible"

    # Form the council
    council = []
    for member in council_members:
        club = club_representatives[member]
        council.append((member, club))

    # Return the council
    return council

