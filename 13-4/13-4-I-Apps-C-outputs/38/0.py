
def solve(n, residents):
    # Initialize the council members and the clubs they represent
    council_members = {}
    clubs = {}

    # Iterate through the residents and their clubs
    for resident in residents:
        # Get the resident's name, party, and clubs
        name, party, num_clubs, *club_names = resident.split()

        # If the resident is not already a council member, add them to the council
        if name not in council_members:
            council_members[name] = party

        # Add the resident to the club they represent
        for club_name in club_names:
            if club_name not in clubs:
                clubs[club_name] = set()
            clubs[club_name].add(name)

    # Check if the council is valid
    for club_name, club_members in clubs.items():
        # If the number of council members in the same party as the club is greater than or equal to half the number of council members, return "Impossible"
        if len(club_members.intersection(council_members.values())) >= len(council_members) // 2:
            return "Impossible"

    # If the council is valid, return the council members and the clubs they represent
    return "\n".join(f"{name} {club_name}" for name, club_name in council_members.items())

