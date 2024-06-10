
def is_divisible_by_25(n):
    while n % 25 != 0:
        n = swap_adjacent_digits(n)
        if n == 0:
            return -1
    return n

def swap_adjacent_digits(n):
    n = str(n)
    n = n[0] + n[2] + n[1] + n[3] + n[4]
    return int(n)

if __name__ == '__main__':
    n = int(input())
    print(is_divisible_by_25(n))

