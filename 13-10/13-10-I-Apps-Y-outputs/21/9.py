
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
        n = n - (n & -n)
    return count

if __name__ == '__main__':
    n = int(input("Enter a binary string: "))
    print(f"The number of '1' bits in the binary string {n} is: {count_ones(n)}")
    print(f"The optimized number of '1' bits in the binary string {n} is: {count_ones_optimized(n)}")

