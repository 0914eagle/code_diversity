
def is_divisible(n, a):
    return n % a == 0

def is_square(n):
    return int(n**0.5)**2 == n

def get_largest_lovely_number(n):
    for i in range(n, 1, -1):
        if not any(is_divisible(i, a) for a in range(2, int(i**0.5) + 1)):
            return i
    return 1

def main():
    n = int(input())
    print(get_largest_lovely_number(n))

if __name__ == '__main__':
    main()

