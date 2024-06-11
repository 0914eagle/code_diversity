def count_up_to(n):
    
    if n <= 1:
        return []
    primes = [2]
    for i in range(3, n, 2):
        for j in primes:
            if j > int(i ** 0.5) + 1:
                primes.append(i)
                break
            if i % j == 0:
                break
    return primes


if __name__ == "__main__":
    print(count_up_to(5))
    print(count_up_to(11))
    print(count_up_to(0))
    print(count_up_to(20))
    print(count_up_to(1))
    print(count_up_to(18))
