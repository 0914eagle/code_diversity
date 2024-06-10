
def get_sequence_digit(k):
    # Find the block that contains the digit at position k
    block_size = 1
    while k > block_size:
        k -= block_size
        block_size += 1
    
    # Return the digit at position k in the block
    return str(block_size)[k - 1]

def main():
    q = int(input())
    for i in range(q):
        k = int(input())
        print(get_sequence_digit(k))

if __name__ == '__main__':
    main()

