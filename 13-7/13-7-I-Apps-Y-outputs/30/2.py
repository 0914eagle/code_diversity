
def get_digit_at_position(position):
    # Find the block that contains the given position
    block_size = 1
    while position > block_size:
        position -= block_size
        block_size += 1
    
    # Find the digit within the block
    digit = 1
    for _ in range(block_size - 1):
        digit += 1
    
    return digit

def solve(queries):
    for query in queries:
        print(get_digit_at_position(query))

if __name__ == '__main__':
    q = int(input())
    queries = [int(input()) for _ in range(q)]
    solve(queries)

