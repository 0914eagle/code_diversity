
def is_sum_of_cubes(n):
    for i in range(1, int(n**(1/3))):
        j = n - i**3
        if j >= 0 and j**(1/3) % 1 == 0:
            return True
    return False

def find_largest_bus_number(m):
    for i in range(m, 0, -1):
        if is_sum_of_cubes(i):
            return i
    return None

