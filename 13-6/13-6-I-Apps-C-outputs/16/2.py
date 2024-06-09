
def get_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if n // i != i:
                divisors.append(n // i)
    divisors.sort()
    return divisors

def get_aesthetic_colors(n):
    divisors = get_divisors(n)
    return len(set(divisors))

def main():
    n = int(input())
    print(get_aesthetic_colors(n))

if __name__ == '__main__':
    main()

