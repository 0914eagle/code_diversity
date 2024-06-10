
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def input_numbers():
    a, b = map(int, input().split())
    return a, b

def main():
    a, b = input_numbers()
    print(gcd(a, b))

if __name__ == '__main__':
    main()

