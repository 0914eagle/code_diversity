
def get_sequence_element(k):
    # Find the block that contains the element at position k
    block_size = 1
    while k > block_size:
        block_size += 1
    # Find the element within the block
    element = k - (block_size - 1)
    # Calculate the value of the element
    value = 1
    for i in range(1, element + 1):
        value += 1
    return value % 10

def main():
    q = int(input())
    for i in range(q):
        k = int(input())
        print(get_sequence_element(k))

if __name__ == '__main__':
    main()

