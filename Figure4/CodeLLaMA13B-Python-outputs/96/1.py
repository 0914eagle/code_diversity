def count_up_to(n):
    
    # Your code here
    if n < 0:
        return []
    elif n == 0:
        return []
    else:
        primes = []
        for i in range(2, n):
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                primes.append(i)
        return primes