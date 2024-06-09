
def f1(n, residents):
    # Initialize variables
    council_members = []
    clubs = []

    # Iterate through each resident
    for resident in residents:
        # Get the resident's information
        name, party, num_clubs, club_names = resident

        # Check if the resident is already a council member
        if name in council_members:
            continue

        # Check if the resident belongs to any clubs
        if num_clubs == 0:
            continue

        # Check if the resident belongs to more than one club
        if num_clubs > 1:
            # Select the first club the resident belongs to
            club = club_names[0]
        else:
            # Select the only club the resident belongs to
            club = club_names[0]

        # Add the resident to the council
        council_members.append(name)
        clubs.append(club)

    # Check if the number of council members belonging to any given party does not exceed half the membership of the council
    if len(council_members) % 2 == 0:
        half = len(council_members) // 2
    else:
        half = (len(council_members) // 2) + 1

    parties = {}
    for name in council_members:
        party = residents[name][1]
        if party not in parties:
            parties[party] = 1
        else:
            parties[party] += 1

    for party, num_members in parties.items():
        if num_members > half:
            return "Impossible"

    # Return the council members and the clubs they represent
    return "\n".join([f"{name} {club}" for name, club in zip(council_members, clubs)])

def f2(...):
    # Implement f2 here
    pass

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        residents = {}
        for _ in range(n):
            name, party, num_clubs, club_names = input().split()
            residents[name] = (name, party, int(num_clubs), club_names.split(","))
        print(f1(n, residents))

