
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

def main():
    n = int(input())
    lovely_numbers = []
    for i in range(1, n+1):
        if is_lovely(i):
            lovely_numbers.append(i)
    print(max(lovely_numbers))

if __name__ == '__main__':
    main()

