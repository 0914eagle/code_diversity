
def is_good_number(n):
    while n > 0:
        if n % 3 == 0:
            n /= 3
        else:
            return False
    return True


def find_smallest_good_number(n):
    while not is_good_number(n):
        n += 1
    return n


q = int(input())
for _ in range(q):
    n = int(input())
    print(find_smallest_good_number(n))

