def is_multiply_prime(a):
    
    # Find the prime numbers
    prime_numbers = []
    for i in range(2, a):
        if is_prime(i):
            prime_numbers.append(i)
    # Check if the number is the multiplication of 3 prime numbers
    if len(prime_numbers) >= 3:
        for i in range(len(prime_numbers) - 2):
            for j in range(i + 1, len(prime_numbers) - 1):
                for k in range(j + 1, len(prime_numbers)):
                    if prime_numbers[i] * prime_numbers[j] * prime_numbers[k] == a:
                        return True
    return False


