
def is_easily_playable(s):
    if len(s) % 2 == 1:
        return "No"
    
    for i in range(len(s)):
        if i % 2 == 0:
            if s[i] not in "LUDR":
                return "No"
        else:
            if s[i] not in "RUDR":
                return "No"
    
    return "Yes"

