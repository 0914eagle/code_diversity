
def solve(a, x):
    # Calculate the prime factorization of all numbers in the sequence
    prime_factors = [[] for _ in range(len(a))]
    for i, num in enumerate(a):
        prime_factors[i] = list(prime_factorization(num))

    # Initialize the result with the number of pairs (l, r) such that gcd(a_l, a_l + 1, ..., a_r) = x
    result = 0

    # Iterate over each query x_i
    for i in range(len(x)):
        # Initialize the number of pairs (l, r) such that gcd(a_l, a_l + 1, ..., a_r) = x_i to 0
        count = 0

        # Iterate over each number in the sequence
        for j in range(len(a)):
            # If the gcd of the prime factors of a_j and a_j + 1 is x_i, increment the count
            if gcd_prime_factors(prime_factors[j], prime_factors[j + 1]) == x[i]:
                count += 1

        # Add the count to the result
        result += count

    return result

# Calculate the gcd of two lists of prime factors
def gcd_prime_factors(p1, p2):
    result = []
    i, j = 0, 0
    while i < len(p1) and j < len(p2):
        if p1[i] == p2[j]:
            result.append(p1[i])
            i += 1
            j += 1
        elif p1[i] < p2[j]:
            i += 1
        else:
            j += 1
    return result

# Calculate the prime factorization of a number
def prime_factorization(n):
    if n == 1:
        return [1]
    factors = []
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            factors.append(i)
            while n % i == 0:
                n //= i
    if n > 1:
        factors.append(n)
    return factors

