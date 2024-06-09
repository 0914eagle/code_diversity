
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


def solve(queries):
    for query in queries:
        print(find_next_good_number(query))


solve([1, 2, 6, 13, 14, 3620, 10000, 1000000000000000000])

