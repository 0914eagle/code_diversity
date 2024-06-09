
def get_bus_number(m):
    for i in range(m, 0, -1):
        if is_bus_number(i):
            return i
    return None

def is_bus_number(n):
    for i in range(1, int(n**(1/3))):
        for j in range(i, int(n**(1/3))):
            if i**3 + j**3 == n:
                return True
    return False

