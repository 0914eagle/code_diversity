
def is_good_number(n):
    while n > 3:
        if n % 3 != 0:
            return False
        n //= 3
    return True


def find_smallest_good_number(n):
    while not is_good_number(n):
        n += 1
    return n


def main():
    q = int(input())
    for _ in range(q):
        n = int(input())
        print(find_smallest_good_number(n))


if __name__ == '__main__':
    main()

