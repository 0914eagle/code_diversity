def count_up_to(n):
    
    # Your code here
    if n <= 1:
        return []
    primes = [2]
    for i in range(3, n, 2):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            primes.append(i)
    return primes


print(count_up_to(18))
