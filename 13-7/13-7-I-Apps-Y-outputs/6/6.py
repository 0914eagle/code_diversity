
def is_easily_playable(s):
    if len(s) % 2 == 0:
        return "No"
    for i in range(len(s)):
        if i % 2 == 0 and s[i] not in "LUDR":
            return "No"
        if i % 2 == 1 and s[i] not in "RULD":
            return "No"
    return "Yes"

