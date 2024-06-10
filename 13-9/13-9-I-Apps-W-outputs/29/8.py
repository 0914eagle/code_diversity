
def get_input():
    a, b = map(int, input().split())
    return a, b

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def solve(a, b):
    result = 1
    for i in range(a, b+1):
        result = gcd(result, i)
    return result

def main():
    a, b = get_input()
    print(solve(a, b))

if __name__ == '__main__':
    main()

