
def is_elegant(n):
    factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
            continue
        factors.append(i)
        n //= i
    if n > 1:
        factors.append(n)
    gcd = 1
    for f in factors:
        gcd = gcd_recursive(gcd, f)
    return gcd == 1

def gcd_recursive(a, b):
    if b == 0:
        return a
    return gcd_recursive(b, a % b)

def count_elegant(n):
    count = 0
    for i in range(2, n + 1):
        if is_elegant(i):
            count += 1
    return count

def main():
    num_cases = int(input())
    for _ in range(num_cases):
        n = int(input())
        print(count_elegant(n))

if __name__ == '__main__':
    main()

