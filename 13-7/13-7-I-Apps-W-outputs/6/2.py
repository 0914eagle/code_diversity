
def is_perfect_square(n):
    
    sqrt_n = int(n**0.5)
    return sqrt_n**2 == n

def get_divisors(n):
    
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i*i != n:
                divisors.append(n//i)
    divisors.sort(reverse=True)
    return divisors

def get_biggest_lovely_number(n):
    
    divisors = get_divisors(n)
    for d in divisors:
        if not is_perfect_square(d):
            return d
    return n

if __name__ == '__main__':
    n = int(input())
    print(get_biggest_lovely_number(n))

