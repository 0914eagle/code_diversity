
def find_beautiful_number(p, x):
    if x == 1:
        return "Impossible"
    
    for i in range(10**(p-1), 10**p):
        if str(i) == str(i*x)[1:]:
            return str(i)
    
    return "Impossible"

