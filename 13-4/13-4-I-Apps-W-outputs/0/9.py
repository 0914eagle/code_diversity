
def is_possible(s):
    amber, buff, canary = 0, 0, 0
    for i in range(len(s)):
        if s[i] == "A":
            amber += 1
        elif s[i] == "B":
            buff += 1
        elif s[i] == "C":
            canary += 1
    
    return "Yes" if amber > 0 and buff > 0 and canary > 0 else "No"

