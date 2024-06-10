
def get_hamming_weight(n):
    
    return bin(n).count("1")

def get_hamming_weight_optimized(n):
    
    return n.count("1")

if __name__ == '__main__':
    n = input("Enter an unsigned integer: ")
    print(get_hamming_weight(n))

