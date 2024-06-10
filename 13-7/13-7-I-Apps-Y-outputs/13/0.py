
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_between(n, a, b):
    return a <= n <= b

def is_odd(n):
    return n % 2 == 1

def is_even(n):
    return n % 2 == 0

def guess_number(n, k):
    if k == 0:
        return 1
    if k == 1:
        return n
    if k == 2:
        return 1 if is_prime(n) else n
    if k == 3:
        return 1 if is_between(n, 1, 10) else n
    if k == 4:
        return 1 if is_odd(n) else n
    if k == 5:
        return 1 if is_even(n) else n
    if k == 6:
        return 1 if is_prime(n) and is_between(n, 1, 10) else n
    if k == 7:
        return 1 if is_prime(n) and is_odd(n) else n
    if k == 8:
        return 1 if is_prime(n) and is_even(n) else n
    if k == 9:
        return 1 if is_between(n, 1, 10) and is_odd(n) else n
    if k == 10:
        return 1 if is_between(n, 1, 10) and is_even(n) else n
    return n

def main():
    n, k = map(int, input().split())
    print("Your wish is granted!" if guess_number(n, k) == 1 else "You will become a flying monkey!")

if __name__ == '__main__':
    main()

