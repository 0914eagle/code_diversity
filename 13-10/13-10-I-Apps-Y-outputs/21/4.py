
def get_hamming_weight(n):
    
    return bin(n).count("1")

def get_hamming_weight_optimized(n):
    
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count

if __name__ == '__main__':
    n = int(input("Enter an unsigned integer: "))
    print(f"The number of '1' bits in the binary representation of {n} is {get_hamming_weight(n)}")
    print(f"The number of '1' bits in the binary representation of {n} is {get_hamming_weight_optimized(n)}")

