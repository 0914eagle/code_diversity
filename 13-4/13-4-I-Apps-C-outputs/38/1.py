
def solve(n, residents):
    # Initialize variables
    council_members = []
    clubs = []
    parties = []

    # Iterate through each resident
    for resident in residents:
        # Get the resident's information
        name, party, num_clubs, *club_names = resident.split()

        # Add the resident to the council if they are not already on it
        if name not in council_members:
            council_members.append(name)

        # Add the resident's party to the list of parties
        parties.append(party)

        # Add the resident's clubs to the list of clubs
        clubs.extend(club_names)

    # Check if the number of council members belonging to any given party does not exceed half the membership of the council
    if len(council_members) % 2 == 0:
        max_members_per_party = len(council_members) // 2
    else:
        max_members_per_party = (len(council_members) // 2) + 1

    # Initialize a dictionary to store the number of council members per party
    num_council_members_per_party = {}
    for party in parties:
        num_council_members_per_party[party] = 0

    # Iterate through each council member and increment the number of council members per party
    for council_member in council_members:
        party = council_member.split()[1]
        num_council_members_per_party[party] += 1

    # Check if the number of council members per party does not exceed the maximum allowed
    for party, num_members in num_council_members_per_party.items():
        if num_members > max_members_per_party:
            return "Impossible"

    # Return the council members and their clubs
    return "\n".join([f"{council_member} {club}" for council_member, club in zip(council_members, clubs)])

