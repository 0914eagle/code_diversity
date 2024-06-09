
def solve(residents, parties, clubs):
    # Initialize the dictionary to store the club representatives
    club_representatives = {}

    # Loop through each resident
    for resident in residents:
        # Get the resident's party and clubs
        party = resident[1]
        clubs = resident[2:]

        # Loop through each club
        for club in clubs:
            # If the club does not have a representative yet, assign the resident as the representative
            if club not in club_representatives:
                club_representatives[club] = resident
            # If the club already has a representative, check if the resident's party is different from the representative's party
            else:
                representative = club_representatives[club]
                if representative[1] != party:
                    # If the parties are different, assign the resident as the representative
                    club_representatives[club] = resident

    # Return the club representatives
    return club_representatives

