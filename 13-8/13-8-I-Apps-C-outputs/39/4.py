
def solve_problem(n, residents):
    # Initialize variables
    council_members = []
    club_representatives = {}
    parties = {}

    # Iterate through each resident
    for resident in residents:
        # Get the resident's information
        resident_name, party, num_clubs, *clubs = resident.split()

        # If the resident is not already a council member
        if resident_name not in council_members:
            # Add the resident to the council
            council_members.append(resident_name)

            # Assign a club representative for the resident
            club_representatives[resident_name] = clubs[0]

            # Update the party information
            if party not in parties:
                parties[party] = 1
            else:
                parties[party] += 1

    # Check if the number of council members from each party does not exceed half the membership of the council
    for party, num_members in parties.items():
        if num_members > n // 2:
            return "Impossible"

    # Return the council members and their clubs
    return "\n".join([f"{member} {club_representatives[member]}" for member in council_members])

