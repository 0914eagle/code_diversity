
def get_digit(k):
    # Find the block that contains the digit
    block_size = 1
    while k > block_size:
        k -= block_size
        block_size += 1
    
    # Return the digit
    return str(block_size)[-1]

def main():
    q = int(input())
    for _ in range(q):
        k = int(input())
        print(get_digit(k))

if __name__ == '__main__':
    main()

