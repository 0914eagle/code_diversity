
def is_easily_playable(s):
    if len(s) < 1 or len(s) > 100:
        return "No"
    for i, c in enumerate(s):
        if i % 2 == 0 and c not in "LUD":
            return "No"
        if i % 2 == 1 and c not in "RUD":
            return "No"
    return "Yes"

