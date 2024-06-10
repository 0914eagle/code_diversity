
def sequence_element(k):
    # Find the block of numbers that contains the k-th element
    block_size = 1
    while k > block_size:
        k -= block_size
        block_size += 1
    
    # Calculate the position of the element in the block
    position_in_block = k
    
    # Calculate the value of the element
    value = (position_in_block * (position_in_block + 1)) // 2
    
    return value % 10

def main():
    q = int(input())
    for i in range(q):
        k = int(input())
        print(sequence_element(k))

if __name__ == '__main__':
    main()

