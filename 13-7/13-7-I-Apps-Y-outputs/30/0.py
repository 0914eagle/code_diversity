
def get_digit_at_position(position):
    # Find the block that contains the position
    block_size = 1
    while position > block_size:
        position -= block_size
        block_size += 1
    
    # Find the digit within the block
    digit = 1
    while block_size > 1:
        if position == block_size:
            break
        digit += 1
        block_size -= 1
    
    return digit

def main():
    q = int(input())
    for _ in range(q):
        k = int(input())
        print(get_digit_at_position(k))

if __name__ == '__main__':
    main()

