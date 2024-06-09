
def solve(input_data):
    # Initialize variables
    num_test_cases = int(input_data[0])
    output = []

    # Iterate over each test case
    for i in range(1, num_test_cases + 1):
        # Get the number of residents and their information
        num_residents = int(input_data[i])
        residents = input_data[i + 1 : i + 1 + num_residents]

        # Initialize a dictionary to store the club memberships
        club_members = {}

        # Iterate over each resident and their information
        for resident in residents:
            # Split the resident information
            resident_info = resident.split()
            resident_name = resident_info[0]
            resident_party = resident_info[1]
            num_clubs = int(resident_info[2])
            clubs = resident_info[3:]

            # Add the resident to the club memberships
            for club in clubs:
                if club not in club_members:
                    club_members[club] = []
                club_members[club].append(resident_name)

        # Initialize a list to store the council members
        council_members = []

        # Iterate over each club and its members
        for club, members in club_members.items():
            # If the club has more than one member, select one member to represent the club
            if len(members) > 1:
                # Select a member at random
                member = members[0]

                # Add the member to the council members list
                council_members.append((member, club))

                # Remove the member from the club members list
                club_members[club].remove(member)

        # If the council members list is not empty, print the council members
        if council_members:
            output.append(" ".join([member[0] for member in council_members]))
        else:
            output.append("Impossible")

        # Add a blank line between test cases
        output.append("")

    # Return the output
    return "\n".join(output)

