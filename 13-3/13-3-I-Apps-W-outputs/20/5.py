
def find_beautiful_number(p, x):
    for i in range(10**p):
        if str(i).find("0") == -1 and str(i*x).find(str(i)) == 0:
            return str(i)
    return "Impossible"

