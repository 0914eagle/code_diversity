
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_between(n, a, b):
    return a <= n <= b

def is_even(n):
    return n % 2 == 0

def guess_the_number(n, k):
    if k == 0:
        return "Your wish is granted!"
    if n == 1:
        return "You will become a flying monkey!"
    if is_prime(n):
        return guess_the_number(n-1, k-1)
    if is_between(n, 7, 10):
        return guess_the_number(n-1, k-1)
    if is_even(n):
        return guess_the_number(n-1, k-1)
    return "Your wish is granted!"

if __name__ == '__main__':
    n, k = map(int, input().split())
    print(guess_the_number(n, k))

