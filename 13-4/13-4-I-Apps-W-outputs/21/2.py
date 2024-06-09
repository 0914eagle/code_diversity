
def solve(a, b):
    if a == 0 and b == 0:
        return "YES"
    
    while a > 0 and b > 0:
        if a > b:
            a = a - b
        else:
            b = b - a
    
    if a == 0 and b == 0:
        return "YES"
    else:
        return "NO"

