
def get_number_of_different_purchases(num_clients, clients, colored_limit, bw_limit):
    # Initialize a set to store the different purchases
    purchases = set()
    
    # Iterate over the clients and their requirements
    for client, color_limit, bw_limit in clients:
        # If the client wants at least one colored painting
        if color_limit > 0:
            # Add the client to the set of purchases
            purchases.add((client, color_limit, 0))
        
        # If the client wants at least one black and white painting
        if bw_limit > 0:
            # Add the client to the set of purchases
            purchases.add((client, 0, bw_limit))
    
    # Return the number of different purchases
    return len(purchases)

def main():
    # Read the input
    num_clients, colored_limit, bw_limit = map(int, input().split())
    clients = []
    for _ in range(num_clients):
        clients.append(tuple(map(int, input().split())))
    num_changes = int(input())
    changes = []
    for _ in range(num_changes):
        changes.append(tuple(map(int, input().split())))
    
    # Initialize the number of different purchases
    num_different_purchases = get_number_of_different_purchases(num_clients, clients, colored_limit, bw_limit)
    
    # Iterate over the changes and update the number of different purchases
    for client, color_limit, bw_limit in changes:
        # If the client wants at least one colored painting
        if color_limit > 0:
            # Add the client to the set of purchases
            purchases.add((client, color_limit, 0))
        
        # If the client wants at least one black and white painting
        if bw_limit > 0:
            # Add the client to the set of purchases
            purchases.add((client, 0, bw_limit))
        
        # Update the number of different purchases
        num_different_purchases = len(purchases)
    
    # Print the number of different purchases
    print(num_different_purchases)

if __name__ == '__main__':
    main()

