
def number_of_purchases(N, C, a, b):
    # Initialize a list to store the number of purchases for each client
    purchases = [0] * (N + 1)
    # Initialize a list to store the number of colored paintings for each client
    colored_paintings = [0] * (N + 1)
    # Initialize a list to store the number of black and white paintings for each client
    black_and_white_paintings = [0] * (N + 1)
    
    # Loop through each client and update the number of purchases, colored paintings, and black and white paintings
    for i in range(1, N + 1):
        purchases[i] = max(a[i - 1], b[i - 1])
        colored_paintings[i] = a[i - 1]
        black_and_white_paintings[i] = b[i - 1]
    
    # Initialize a set to store the unique purchases
    unique_purchases = set()
    
    # Loop through each client and add the number of purchases to the set of unique purchases
    for i in range(1, N + 1):
        unique_purchases.add(purchases[i])
    
    # Loop through each client and add the number of colored paintings to the set of unique purchases
    for i in range(1, N + 1):
        if colored_paintings[i] > 0:
            unique_purchases.add(colored_paintings[i])
    
    # Loop through each client and add the number of black and white paintings to the set of unique purchases
    for i in range(1, N + 1):
        if black_and_white_paintings[i] > 0:
            unique_purchases.add(black_and_white_paintings[i])
    
    # Return the number of unique purchases that are at least C
    return len([purchase for purchase in unique_purchases if purchase >= C])

def handle_changes(N, C, a, b, Q, changes):
    # Loop through each requirement change
    for change in changes:
        # Update the number of paintings for the client
        a[change[0] - 1] = change[1]
        b[change[0] - 1] = change[2]
    
    # Return the number of different purchases
    return number_of_purchases(N, C, a, b)

def main():
    # Read the input
    N, C = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    Q = int(input())
    changes = []
    for _ in range(Q):
        changes.append(list(map(int, input().split())))
    
    # Call the function to handle the changes
    result = handle_changes(N, C, a, b, Q, changes)
    
    # Print the result
    print(result)

if __name__ == '__main__':
    main()

