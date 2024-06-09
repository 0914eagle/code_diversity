
def get_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if n // i != i:
                divisors.append(n // i)
    divisors.sort(reverse=True)
    return divisors

def get_min_tax(n):
    divisors = get_divisors(n)
    min_tax = 0
    for d in divisors:
        if d >= 2:
            min_tax += 1
        else:
            break
    return min_tax

def get_optimal_split(n):
    divisors = get_divisors(n)
    optimal_split = []
    for d in divisors:
        if d >= 2:
            optimal_split.append(d)
        else:
            break
    return optimal_split

def main():
    n = int(input())
    print(get_min_tax(n))

if __name__ == '__main__':
    main()

