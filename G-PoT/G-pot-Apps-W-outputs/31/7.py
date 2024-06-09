
def find_beautiful_divisor(n):
    for i in range(1, n+1):
        if n % i == 0:
            if (i & (i + 1)) == 0:
                return n // i

n = int(input())
print(find_beautiful_divisor(n))
