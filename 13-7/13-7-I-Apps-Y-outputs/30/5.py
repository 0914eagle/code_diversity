
def get_digit(n):
    # Calculate the digit at position n of the sequence
    digit = 1
    while n > 0:
        digit += 1
        n -= digit
    return digit

def solve(queries):
    # Iterate over the queries and calculate the digit at the corresponding position
    for query in queries:
        print(get_digit(query))

if __name__ == '__main__':
    q = int(input())
    queries = [int(input()) for _ in range(q)]
    solve(queries)

