def count_up_to(n):
    
    primes = [2, 3, 5, 7, 11, 13, 17, 19]
    result = []
    for i in range(2, n + 1):
        if i in primes:
            result.append(i)
        else:
            for j in primes:
                if i % j == 0:
                    break
            else:
                result.append(i)
    return result


