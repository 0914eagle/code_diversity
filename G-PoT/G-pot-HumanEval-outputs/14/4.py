
def skjkasdkd(lst: List[int]) -> int:
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    primes = [num for num in lst if is_prime(num)]
    if not primes:
        return 0

    max_prime = max(primes)
    digit_sum = sum(int(digit) for digit in str(max_prime))
    return digit_sum
