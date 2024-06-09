
def is_multiply_prime(a: int) -> bool:
    
    if a < 100 and a > 0:
        prime_numbers = []
        for i in range(2, int(a ** 0.5) + 1):
            if a % i == 0:
                prime_numbers.append(i)
        return len(prime_numbers) == 3
    else:
        return False

