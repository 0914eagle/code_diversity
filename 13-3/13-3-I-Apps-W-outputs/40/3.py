
def get_max_score(numbers):
    # Calculate the greatest common divisor of all numbers
    gcd = math.gcd(numbers[0], numbers[1])
    for i in range(2, len(numbers)):
        gcd = math.gcd(gcd, numbers[i])
    return gcd

def get_min_operations(numbers):
    # Calculate the prime factors of all numbers
    prime_factors = [[] for _ in range(len(numbers))]
    for i in range(len(numbers)):
        n = numbers[i]
        while n % 2 == 0:
            prime_factors[i].append(2)
            n //= 2
        for p in range(3, int(math.sqrt(n)) + 1, 2):
            while n % p == 0:
                prime_factors[i].append(p)
                n //= p
        if n > 1:
            prime_factors[i].append(n)
    
    # Find the minimum number of operations required to obtain the maximum score
    min_operations = float('inf')
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            gcd = math.gcd(numbers[i], numbers[j])
            for p in prime_factors[i]:
                if p in prime_factors[j]:
                    operations = 1 + get_min_operations([gcd, numbers[i] // p, numbers[j] // p])
                    if operations < min_operations:
                        min_operations = operations
    
    return min_operations

numbers = [int(x) for x in input().split()]
print(get_max_score(numbers))
print(get_min_operations(numbers))

