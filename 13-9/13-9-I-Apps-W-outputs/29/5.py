
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def gcd_big(a, b):
    if b == 0:
        return a
    else:
        return gcd_big(b, a % b)

def main():
    a, b = map(int, input().split())
    print(gcd_big(a, b))

if __name__ == '__main__':
    main()

