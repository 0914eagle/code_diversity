
def get_digit(k):
    # Find the block that contains the element at position k
    block_size = 1
    while k > block_size:
        k -= block_size
        block_size += 1
    
    # Find the position of the element in the block
    position_in_block = k
    
    # Calculate the value of the element
    value = (position_in_block * (position_in_block + 1)) // 2 + 1
    
    # Return the digit of the value
    return str(value)[-1]

def main():
    q = int(input())
    for i in range(q):
        k = int(input())
        print(get_digit(k))

if __name__ == '__main__':
    main()

