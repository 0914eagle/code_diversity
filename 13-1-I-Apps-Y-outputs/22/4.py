
def is_good_number(n):
    while n > 0:
        if n % 3 == 0:
            n /= 3
        else:
            return False
    return True


def find_next_good_number(n):
    while not is_good_number(n):
        n += 1
    return n


def solve(n):
    return find_next_good_number(n)

