
def get_input():
    return int(input())

def is_odd_with_eight_divisors(n):
    if n % 2 == 0 or n < 1:
        return False
    count = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            count += 2
    return count == 8

def count_odd_numbers_with_eight_divisors(n):
    count = 0
    for i in range(1, n + 1):
        if is_odd_with_eight_divisors(i):
            count += 1
    return count

if __name__ == '__main__':
    n = get_input()
    print(count_odd_numbers_with_eight_divisors(n))

