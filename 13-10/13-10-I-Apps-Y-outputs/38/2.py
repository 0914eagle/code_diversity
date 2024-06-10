
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_min_prime(x):
    for i in range(x, 10**5+1):
        if is_prime(i):
            return i
    return -1

if __name__ == '__main__':
    x = int(input())
    print(find_min_prime(x))

