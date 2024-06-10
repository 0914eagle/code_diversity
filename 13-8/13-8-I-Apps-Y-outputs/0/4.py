
def get_points(x):
    # Find the prime factors of x
    prime_factors = []
    while x % 2 == 0:
        prime_factors.append(2)
        x //= 2
    for i in range(3, int(x**0.5) + 1, 2):
        while x % i == 0:
            prime_factors.append(i)
            x //= i
    if x > 1:
        prime_factors.append(x)
    
    # Calculate the number of points
    points = 0
    for p in prime_factors:
        points += 1 + p
    
    return points

def main():
    x = int(input())
    print(get_points(x))

if __name__ == '__main__':
    main()

