
def get_divisible_digits(k, a):
    # Find the divisible digits in the number system with base k
    divisible_digits = []
    for i in range(k):
        if a % k == i:
            divisible_digits.append(i)
    return divisible_digits

def get_happy_digits(k, a, divisible_digits):
    # Find the happy digits in the number system with base k
    happy_digits = []
    for i in range(k):
        if i in divisible_digits and a % (k**i) == 0:
            happy_digits.append(i)
    return happy_digits

def get_happy_values(k, a, divisible_digits):
    # Find the happy values in the number system with base k
    happy_values = []
    for i in range(k):
        if i in divisible_digits:
            happy_values.append(a * (k**i))
    return happy_values

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    divisible_digits = get_divisible_digits(k, a)
    happy_digits = get_happy_digits(k, a, divisible_digits)
    happy_values = get_happy_values(k, a, divisible_digits)
    print(len(happy_digits))
    print(*happy_values)

if __name__ == '__main__':
    main()

