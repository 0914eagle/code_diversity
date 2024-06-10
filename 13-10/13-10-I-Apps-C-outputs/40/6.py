
def get_number_of_purchases(N, C, a, b):
    # Initialize a list to store the number of purchases for each client
    purchases = [0] * (N + 1)
    # Initialize a list to store the number of colored paintings for each client
    colored_paintings = [0] * (N + 1)
    # Initialize a list to store the number of black and white paintings for each client
    black_and_white_paintings = [0] * (N + 1)

    # Loop through each client and calculate the number of purchases for that client
    for i in range(1, N + 1):
        # If the client wants colored paintings
        if a[i] > 0:
            # Calculate the number of colored paintings the client can purchase
            num_colored_paintings = min(a[i], b[i])
            # Update the number of purchases for the client
            purchases[i] += num_colored_paintings
            # Update the number of colored paintings for the client
            colored_paintings[i] += num_colored_paintings
        # If the client wants black and white paintings
        if b[i] > 0:
            # Calculate the number of black and white paintings the client can purchase
            num_black_and_white_paintings = b[i] - a[i]
            # Update the number of purchases for the client
            purchases[i] += num_black_and_white_paintings
            # Update the number of black and white paintings for the client
            black_and_white_paintings[i] += num_black_and_white_paintings

    # Initialize a variable to store the number of different purchases
    num_different_purchases = 0
    # Loop through each client and calculate the number of different purchases for that client
    for i in range(1, N + 1):
        # If the client has at least one colored painting
        if colored_paintings[i] > 0:
            # Calculate the number of different purchases for the client
            num_different_purchases += (colored_paintings[i] * (colored_paintings[i] + 1)) // 2
        # If the client has at least one black and white painting
        if black_and_white_paintings[i] > 0:
            # Calculate the number of different purchases for the client
            num_different_purchases += (black_and_white_paintings[i] * (black_and_white_paintings[i] + 1)) // 2

    # Return the number of different purchases modulo 10007
    return num_different_purchases % 10007

def main():
    # Read the input
    N, C = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    Q = int(input())
    for _ in range(Q):
        P, a_P, b_P = map(int, input().split())
        a[P] = a_P
        b[P] = b_P
    # Calculate the number of different purchases
    num_different_purchases = get_number_of_purchases(N, C, a, b)
    # Print the number of different purchases
    print(num_different_purchases)

if __name__ == '__main__':
    main()

