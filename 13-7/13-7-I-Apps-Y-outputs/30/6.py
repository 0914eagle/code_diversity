
def get_digit(k):
    # Calculate the block number that contains the digit at position k
    block_num = (k - 1) // 9

    # Calculate the position of the digit within the block
    digit_pos = (k - 1) % 9

    # Calculate the value of the digit
    digit = (block_num * (block_num + 1)) // 2 + digit_pos + 1

    return digit

def solve(queries):
    for query in queries:
        print(get_digit(query))

if __name__ == '__main__':
    q = int(input())
    queries = [int(input()) for _ in range(q)]
    solve(queries)

