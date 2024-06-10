
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def input_numbers():
    a, b = map(int, input().split())
    return a, b

def find_gcd(a, b):
    return gcd(a, b)

def main():
    a, b = input_numbers()
    print(find_gcd(a, b))

if __name__ == '__main__':
    main()

