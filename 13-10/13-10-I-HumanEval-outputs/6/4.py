
def is_multiply_prime(a: int) -> bool:
    
    if a < 100 and a > 0:
        prime_numbers = []
        for i in range(2, a):
            if a % i == 0:
                prime_numbers.append(i)
        if len(prime_numbers) == 3:
            return True
        else:
            return False
    else:
        return False

