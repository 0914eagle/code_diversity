
def get_lcm(n):
    # find the prime factors of n
    prime_factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            prime_factors.append(i)
    if n > 1:
        prime_factors.append(n)
    
    # find the maximum LCM of three numbers
    lcm = 1
    for i in range(3):
        lcm *= prime_factors[i]
    
    return lcm

def main():
    n = int(input())
    print(get_lcm(n))

if __name__ == '__main__':
    main()

