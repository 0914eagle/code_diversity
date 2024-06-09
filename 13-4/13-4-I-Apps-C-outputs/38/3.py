
def get_council_members(residents):
    council_members = []
    for resident in residents:
        club_representatives = {}
        for club in resident.clubs:
            if club not in club_representatives:
                club_representatives[club] = resident
            else:
                return "Impossible"
        council_members.append((resident, club_representatives[resident.clubs[0]]))
    return council_members

