
def is_cube(n):
    x = n ** (1/3)
    return x == int(x)

def is_bus_number(n):
    for i in range(1, int(n ** (1/3)) + 1):
        if is_cube(n - i ** 3):
            return True
    return False

def get_largest_bus_number(m):
    for i in range(m, 0, -1):
        if is_bus_number(i):
            return i
    return None

m = int(input())
print(get_largest_bus_number(m))

