
def get_coins(n, q, a, b):
    # Initialize a dictionary to store the powers of 2
    powers = {2**i: i for i in range(31)}

    # Initialize an array to store the answers
    ans = [-1] * q

    # Iterate over the queries
    for i in range(q):
        # Initialize the minimum number of coins needed
        min_coins = 10**9 + 1

        # Iterate over the coins
        for j in range(n):
            # Check if the current coin can be used to obtain the current query
            if a[j] <= b[i]:
                # Calculate the number of coins needed for the current query
                num_coins = b[i] // a[j]

                # Check if the number of coins needed is less than the minimum
                if num_coins < min_coins:
                    # Update the minimum number of coins needed
                    min_coins = num_coins

        # Check if the minimum number of coins needed is not too large
        if min_coins <= 10**9:
            # Update the answer for the current query
            ans[i] = min_coins

    return ans

def main():
    # Read the input
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    # Solve the problem
    ans = get_coins(n, q, a, b)

    # Print the answer
    print(*ans, sep='\n')

if __name__ == '__main__':
    main()

