
def solve(A, B, X):
    # Initialize variables
    max_integer = 0
    current_integer = 1
    current_price = A * current_integer + B * len(str(current_integer))

    # Loop through integers until the price is greater than the given amount
    while current_price <= X:
        max_integer = current_integer
        current_integer += 1
        current_price = A * current_integer + B * len(str(current_integer))

    # Return the maximum integer that can be bought
    return max_integer

def main():
    A, B, X = map(int, input().split())
    print(solve(A, B, X))

if __name__ == '__main__':
    main()

