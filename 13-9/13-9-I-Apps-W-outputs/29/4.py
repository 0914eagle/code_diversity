
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def gcd_efficient(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def input_numbers():
    a, b = map(int, input().split())
    return a, b

def main():
    a, b = input_numbers()
    print(gcd_efficient(a, b))

if __name__ == '__main__':
    main()

