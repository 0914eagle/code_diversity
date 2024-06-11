def count_up_to(n):
    
    if n < 0:
        return []
    primes = []
    for i in range(2, n + 1):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return primes


print(count_up_to(5))
print(count_up_to(11))
print(count_up_to(0))
print(count_up_to(20))
print(count_up_to(1))
print(count_up_to(18))
