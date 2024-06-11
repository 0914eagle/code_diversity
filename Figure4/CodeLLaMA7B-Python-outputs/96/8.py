def count_up_to(n):
    
    prime_numbers = []
    for i in range(2, n):
        if is_prime(i):
            prime_numbers.append(i)
        if len(prime_numbers) == n:
            break
    return prime_numbers


