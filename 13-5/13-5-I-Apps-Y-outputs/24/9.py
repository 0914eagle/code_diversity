
def is_good_number(n):
    if n == 1:
        return True
    if n % 3 == 0:
        return False
    while n % 3 == 1:
        n //= 3
    return n % 3 == 1

def find_next_good_number(n):
    while not is_good_number(n):
        n += 1
    return n

def solve(queries):
    for query in queries:
        print(find_next_good_number(query))

solve([1, 2, 6, 13, 14, 3620, 10000, 1000000000000000000])

