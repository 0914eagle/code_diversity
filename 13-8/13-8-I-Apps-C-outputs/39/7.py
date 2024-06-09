
def solve_town_council(residents, parties, clubs, num_council_members):
    # Initialize a dictionary to store the candidates for each club
    club_candidates = {}
    for club in clubs:
        club_candidates[club] = None

    # Iterate through the residents and assign them to a club
    for resident in residents:
        # Get the resident's party and the clubs they belong to
        party = parties[resident]
        clubs_for_resident = clubs[resident]

        # Iterate through the clubs the resident belongs to
        for club in clubs_for_resident:
            # If the club doesn't have a candidate yet, assign the resident as the candidate
            if club_candidates[club] is None:
                club_candidates[club] = resident
            # If the club already has a candidate, check if the resident's party is different from the current candidate's party
            else:
                current_candidate = club_candidates[club]
                current_candidate_party = parties[current_candidate]
                if party != current_candidate_party:
                    # If the parties are different, assign the resident as the candidate for the club
                    club_candidates[club] = resident

    # Initialize a list to store the council members
    council_members = []

    # Iterate through the clubs and add the candidates to the council
    for club in club_candidates:
        council_members.append(club_candidates[club])

    # If the number of council members is less than the number of clubs, return "Impossible"
    if len(council_members) < len(clubs):
        return "Impossible"

    # Return the council members and the clubs they represent
    return "\n".join([f"{member} {club}" for member, club in zip(council_members, clubs)])

