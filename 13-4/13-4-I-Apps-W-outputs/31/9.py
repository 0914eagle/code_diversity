
def find_beautiful_number(p, x):
    if x == 1:
        return "Impossible"
    
    for i in range(10**(p-1), 10**p):
        if str(i) != str(i)[:1] + str(i)[1:] * (x-1):
            continue
        return str(i)
    
    return "Impossible"

