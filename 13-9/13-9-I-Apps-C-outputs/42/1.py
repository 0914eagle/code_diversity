
def is_divisibility_hack_valid(b, d):
    if b == 1 or d == 1:
        return "yes"
    
    for m in range(1, d):
        if (b ** m - 1) % d == 0:
            return "yes"
    
    return "no"

