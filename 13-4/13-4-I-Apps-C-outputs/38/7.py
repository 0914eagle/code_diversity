
def solve(n, residents):
    # Initialize the council members and clubs dictionaries
    council_members = {}
    clubs = {}
    
    # Iterate over the residents and their clubs
    for resident, party, num_clubs, *club_names in residents:
        # If the resident is not already a council member, add them to the council
        if resident not in council_members:
            council_members[resident] = party
        
        # Add the resident to the club(s) they belong to
        for club_name in club_names:
            if club_name not in clubs:
                clubs[club_name] = {resident: party}
            else:
                clubs[club_name][resident] = party
    
    # Iterate over the clubs and assign a council member to each club
    for club_name, residents in clubs.items():
        # If the club has more than one resident, choose the resident with the same party as the council member
        if len(residents) > 1:
            for resident, party in residents.items():
                if party == council_members[resident]:
                    clubs[club_name] = {resident: party}
                    break
        
        # If the club has only one resident, assign that resident as the council member
        elif len(residents) == 1:
            for resident, party in residents.items():
                clubs[club_name] = {resident: party}
    
    # Return the council members and clubs
    return council_members, clubs

