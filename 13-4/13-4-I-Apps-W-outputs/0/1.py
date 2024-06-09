
def is_possible(s):
    amber, buff, canary = 0, 0, 0
    for c in s:
        if c == 'A':
            amber += 1
        elif c == 'B':
            buff += 1
        elif c == 'C':
            canary += 1
    
    return "Yes" if amber > 0 and buff > 0 and canary > 0 else "No"

