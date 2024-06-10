
def get_elegant_numbers(n):
    elegant_numbers = 0
    for i in range(2, n+1):
        if gcd(i, i-1) == 1:
            elegant_numbers += 1
    return elegant_numbers

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        print(get_elegant_numbers(n))

