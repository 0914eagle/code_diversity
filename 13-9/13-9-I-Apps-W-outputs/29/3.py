
def greatest_common_divisor(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def find_biggest_divisor(a, b):
    divisor = 1
    while divisor <= b:
        if a % divisor == 0 and b % divisor == 0:
            return divisor
        divisor += 1
    return b

def main():
    a, b = map(int, input().split())
    print(find_biggest_divisor(a, b))

if __name__ == '__main__':
    main()

