
def is_bus_number(n):
    for i in range(1, int(n**(1/3))):
        if n == i**3 + (n-i**3)**3:
            return True
    return False

def largest_bus_number(m):
    for n in range(m, 0, -1):
        if is_bus_number(n):
            return n
    return None

