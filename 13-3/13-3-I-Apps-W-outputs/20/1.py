
def find_beautiful_number(p, x):
    if p == 1:
        return "Impossible"
    
    for i in range(10**(p-1), 10**p):
        if str(i).find("0") == -1 and str(i*x).startswith(str(i)):
            return str(i)
    
    return "Impossible"

