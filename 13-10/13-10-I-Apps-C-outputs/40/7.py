
def get_purchases(N, C, a, b):
    # Initialize a list to store the number of purchases for each client
    purchases = [0] * N

    # Loop through each client and add the maximum number of purchases they can make
    for i in range(N):
        purchases[i] += max(a[i], b[i])

    # Sort the purchases in descending order
    purchases.sort(reverse=True)

    # Initialize a variable to store the number of different purchases
    num_purchases = 0

    # Loop through each client and add the number of purchases they can make if at least C clients get at least one colored painting
    for i in range(N):
        if purchases[i] >= C:
            num_purchases += 1

    return num_purchases

def update_purchases(N, C, a, b, P, a_new, b_new):
    # Update the number of purchases for the client with label P
    a[P-1] = a_new
    b[P-1] = b_new

    # Recompute the number of purchases for each client
    purchases = get_purchases(N, C, a, b)

    return purchases

if __name__ == '__main__':
    N, C = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    Q = int(input())

    # Initialize the number of purchases to 0
    purchases = 0

    # Loop through each requirement change
    for i in range(Q):
        # Read the input for the requirement change
        P, a_new, b_new = map(int, input().split())

        # Update the number of purchases for the client with label P
        purchases = update_purchases(N, C, a, b, P, a_new, b_new)

        # Print the number of different purchases modulo 10007
        print(purchases % 10007)

