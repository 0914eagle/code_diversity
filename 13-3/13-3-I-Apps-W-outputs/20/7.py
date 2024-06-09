
def find_beautiful_number(p, x):
    if x == 1:
        return "Impossible"
    
    for i in range(10**p):
        num = str(i)
        if len(num) == p and num[0] != '0' and int(num) * x == int(num[1:] + num[0]):
            return num
    
    return "Impossible"

