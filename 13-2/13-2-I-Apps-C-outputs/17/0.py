
def get_largest_sum(n):
    for a in range(n+1):
        for b in range(a, n+1):
            if a + b == n:
                return a, b
    return None

def get_sum_of_digits(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum

def get_largest_possible_sum(n):
    a, b = get_largest_sum(n)
    return get_sum_of_digits(a) + get_sum_of_digits(b)

if __name__ == '__main__':
    n = int(input())
    print(get_largest_possible_sum(n))

