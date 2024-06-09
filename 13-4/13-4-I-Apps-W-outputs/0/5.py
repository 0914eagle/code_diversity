
def solve(s):
    amber, buff, canary = 0, 0, 0
    for i in range(len(s)):
        if s[i] == "A":
            amber += 1
        elif s[i] == "B":
            buff += 1
        elif s[i] == "C":
            canary += 1
    
    if amber == 0 or buff == 0 or canary == 0:
        return "No"
    
    if amber == 1 and buff == 1 and canary == 1:
        return "Yes"
    
    if amber == 2 and buff == 1 and canary == 1:
        return "Yes"
    
    if amber == 1 and buff == 2 and canary == 1:
        return "Yes"
    
    if amber == 1 and buff == 1 and canary == 2:
        return "Yes"
    
    return "No"

