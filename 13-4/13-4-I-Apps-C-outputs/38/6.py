
def solve(residents, parties, clubs):
    # Initialize the dictionary to store the club representatives
    club_representatives = {}

    # Iterate through the residents and assign them to clubs
    for resident in residents:
        # Get the resident's party and the number of clubs they belong to
        party = resident[1]
        num_clubs = resident[2]

        # Iterate through the clubs the resident belongs to
        for i in range(num_clubs):
            # Get the name of the club
            club = resident[3 + i]

            # Check if the club already has a representative
            if club not in club_representatives:
                # If not, assign the resident as the representative
                club_representatives[club] = resident[0]
            else:
                # If the club already has a representative, check if the resident's party is different from the current representative's party
                if club_representatives[club] != party:
                    # If the parties are different, assign the resident as the representative
                    club_representatives[club] = resident[0]

    # Return the club representatives
    return club_representatives

