
def count_ones(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count

def count_ones_optimized(n):
    count = 0
    while n:
        count += n & 1
        n = n >> 1
    return count

if __name__ == '__main__':
    n = int(input("Enter a binary string: "))
    print(count_ones(n))
    print(count_ones_optimized(n))

