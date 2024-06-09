
def get_council_members(residents):
    council_members = []
    for resident in residents:
        club = resident["clubs"][0]
        council_members.append({"name": resident["name"], "club": club})
    return council_members

