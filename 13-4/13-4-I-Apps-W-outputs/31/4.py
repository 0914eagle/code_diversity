
def find_beautiful_number(p, x):
    if x == 1:
        return "Impossible"
    
    for i in range(10**(p-1), 10**p):
        if str(i) != "0"*p and str(i*x)[0] == str(i)[-1]:
            return str(i)
    
    return "Impossible"

