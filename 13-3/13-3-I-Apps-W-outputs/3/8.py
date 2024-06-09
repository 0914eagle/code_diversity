
def get_gcd(a, b):
    if b == 0:
        return a
    else:
        return get_gcd(b, a % b)

a, b = map(int, input().split())
print(get_gcd(a, b))

