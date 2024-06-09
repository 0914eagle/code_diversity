
def is_cube_sum(n):
    for i in range(1, int(n**(1/3))):
        if n == i**3 + (n-i**3)**3:
            return True
    return False

def get_bus_numbers(m):
    for i in range(m, 0, -1):
        if is_cube_sum(i):
            return i
    return None

