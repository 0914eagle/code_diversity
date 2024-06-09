
def solve(n, residents):
    # Initialize an empty dictionary to store the club representatives
    representatives = {}

    # Iterate through the residents
    for resident in residents:
        # Get the resident's name, party, and clubs
        name, party, num_clubs, *clubs = resident.split()

        # If the resident is not already a representative
        if name not in representatives:
            # Iterate through the clubs the resident belongs to
            for club in clubs:
                # If the club does not already have a representative
                if club not in representatives:
                    # Assign the resident as the representative for the club
                    representatives[club] = name
                    break

    # Check if all clubs have a representative
    if len(representatives) == n:
        # Return the representatives in the format specified in the problem
        return "\n".join(f"{name} {club}" for club, name in representatives.items())
    else:
        # Return "Impossible" if not all clubs have a representative
        return "Impossible"

