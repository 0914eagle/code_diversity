
def solve(n, residents):
    # Initialize variables
    council_members = []
    parties = {}
    clubs = {}

    # Iterate over the residents
    for resident in residents:
        # Get the resident's information
        name, party, num_clubs, *club_names = resident.split()

        # Add the resident to the party and club dictionaries
        parties[name] = party
        clubs[name] = club_names

        # If the resident is not already on the council, add them
        if name not in council_members:
            council_members.append(name)

    # Iterate over the council members
    for member in council_members:
        # Get the member's information
        name = member
        party = parties[name]
        club_names = clubs[name]

        # Check if the member can represent a club
        if len(club_names) > 0:
            # Get the first club name
            club_name = club_names[0]

            # Check if the member can represent the club
            if club_name not in clubs.values():
                # Add the member to the club dictionary
                clubs[club_name] = [name]
            else:
                # The member cannot represent the club, so remove them from the council
                council_members.remove(name)

    # Check if a council can be formed
    if len(council_members) == 0:
        return "Impossible"

    # Create the output string
    output = ""
    for member in council_members:
        output += member + " " + clubs[member][0] + "\n"

    return output.strip()

