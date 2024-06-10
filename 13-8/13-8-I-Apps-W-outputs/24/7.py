
def is_d_magic(n, d):
    while n > 0:
        if n % 10 == d:
            return True
        n //= 10
    return False

def count_d_magic_numbers(a, b, d):
    count = 0
    for i in range(a, b+1):
        if i % d == 0 and is_d_magic(i, d):
            count += 1
    return count

def main():
    m, d = map(int, input().split())
    a, b = map(int, input().split())
    print(count_d_magic_numbers(a, b, d) % (10**9 + 7))

if __name__ == '__main__':
    main()

