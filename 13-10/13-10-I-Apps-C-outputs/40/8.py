
def get_purchases(N, C, a, b, Q, changes):
    # Initialize a dictionary to store the number of purchases for each client
    purchases = {}
    for i in range(N):
        purchases[i+1] = (a[i], b[i])
    
    # Loop through the requirement changes
    for change in changes:
        # Get the client and their new requirements
        client, a_new, b_new = change
        # Update the client's requirements in the dictionary
        purchases[client] = (a_new, b_new)
    
    # Initialize a variable to store the number of different purchases
    num_purchases = 0
    # Loop through the dictionary of clients and their requirements
    for client, reqs in purchases.items():
        # Get the number of colored and black and white paintings required for this client
        a_req, b_req = reqs
        # If the client requires at least one colored painting, add it to the number of purchases
        if a_req > 0:
            num_purchases += 1
        # If the client requires at least one black and white painting and at least C clients require colored paintings, add it to the number of purchases
        if b_req > 0 and num_purchases >= C:
            num_purchases += 1
    
    # Return the number of different purchases modulo 10000
    return num_purchases % 10007

def main():
    # Read the input
    N, C = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    Q = int(input())
    changes = []
    for _ in range(Q):
        changes.append(list(map(int, input().split())))
    
    # Call the get_purchases function and print the output
    result = get_purchases(N, C, a, b, Q, changes)
    print(result)

if __name__ == '__main__':
    main()

