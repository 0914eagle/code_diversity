
def count_bits(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count

def count_bits_optimized(n):
    count = 0
    while n:
        count += n & 1
        n &= n - 1
    return count

def main():
    n = int(input("Enter a binary string of length 32: "))
    print(count_bits(n))
    print(count_bits_optimized(n))

if __name__ == '__main__':
    main()

