
def get_odd_numbers_with_eight_divisors(n):
    count = 0
    for i in range(1, n+1):
        if i % 2 != 0 and len(list(set(get_divisors(i)))) == 8:
            count += 1
    return count

def get_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i * i != n:
                divisors.append(n // i)
    divisors.sort()
    return divisors

if __name__ == '__main__':
    n = int(input())
    print(get_odd_numbers_with_eight_divisors(n))

