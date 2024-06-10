
def get_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i * i != n:
                divisors.append(n // i)
    divisors.sort(reverse=True)
    return divisors

def is_lovely(n):
    divisors = get_divisors(n)
    for d in divisors:
        if d**2 == n:
            return False
    return True

def get_biggest_lovely(n):
    divisors = get_divisors(n)
    for d in divisors:
        if is_lovely(d):
            return d
    return -1

if __name__ == '__main__':
    n = int(input())
    print(get_biggest_lovely(n))

