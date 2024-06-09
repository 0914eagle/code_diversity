
def solve_problem(n, residents):
    # Initialize variables
    council_members = []
    club_representatives = {}
    impossible = False

    # Iterate through each resident
    for resident in residents:
        # If the resident is already a council member, skip them
        if resident in council_members:
            continue
        # If the resident belongs to only one club, make them the club representative
        if len(resident["clubs"]) == 1:
            club_representatives[resident["clubs"][0]] = resident["name"]
        # If the resident belongs to multiple clubs, check if they are already a council member
        else:
            for club in resident["clubs"]:
                # If the resident is already a council member for a different club, the town cannot be formed
                if club in club_representatives and club_representatives[club] != resident["name"]:
                    impossible = True
                    break
            # If the town can be formed, make the resident the club representative
            if not impossible:
                for club in resident["clubs"]:
                    club_representatives[club] = resident["name"]

    # If the town cannot be formed, return "Impossible"
    if impossible:
        return "Impossible"
    # Otherwise, return the council members and club representatives
    else:
        return "\n".join([f"{club_representatives[club]} {club}" for club in club_representatives])

