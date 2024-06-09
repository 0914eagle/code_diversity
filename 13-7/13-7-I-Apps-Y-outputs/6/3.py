
def is_easily_playable(s):
    if len(s) % 2 == 1:
        return "No"
    
    for i in range(len(s)):
        if i % 2 == 0:
            if s[i] not in "LUD":
                return "No"
        else:
            if s[i] not in "RUD":
                return "No"
    
    return "Yes"

