
def find_end_entrance(n, a, b):
    if b == 0:
        return a
    elif b > 0:
        return (a + b) % n or n
    else:
        return (a - b) % n or n

