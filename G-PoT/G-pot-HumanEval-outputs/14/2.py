
def skjkasdkd(lst: List[int]) -> int:
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def sum_digits(num):
        return sum(int(digit) for digit in str(num))

    prime_numbers = [num for num in lst if is_prime(num)]
    if not prime_numbers:
        return 0

    max_prime = max(prime_numbers)
    return sum_digits(max_prime)
