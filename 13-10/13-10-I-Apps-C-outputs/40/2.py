
def get_number_of_purchases(N, C, a, b):
    # Initialize a dictionary to store the number of purchases for each client
    purchases = {}
    
    # Iterate over the clients and calculate the number of purchases for each client
    for i in range(N):
        # Calculate the number of colored paintings that can be purchased by the current client
        colored_paintings = min(a[i], b[i])
        
        # Add the number of purchases for the current client to the dictionary
        purchases[i] = colored_paintings
    
    # Calculate the total number of purchases
    total_purchases = sum(purchases.values())
    
    # Return the number of purchases modulo 10007
    return total_purchases % 10007

def get_number_of_different_purchases(N, C, a, b, Q, requirements_changes):
    # Initialize a dictionary to store the number of different purchases for each client
    different_purchases = {}
    
    # Iterate over the clients and calculate the number of different purchases for each client
    for i in range(N):
        # Calculate the number of colored paintings that can be purchased by the current client
        colored_paintings = min(a[i], b[i])
        
        # Add the number of different purchases for the current client to the dictionary
        different_purchases[i] = colored_paintings
    
    # Iterate over the requirements changes
    for requirement_change in requirements_changes:
        # Extract the client, the new maximum number of colored paintings, and the new maximum number of black and white paintings
        client, new_a, new_b = requirement_change
        
        # Calculate the new number of colored paintings that can be purchased by the current client
        new_colored_paintings = min(new_a, new_b)
        
        # Update the number of different purchases for the current client
        different_purchases[client] = new_colored_paintings
    
    # Calculate the total number of different purchases
    total_different_purchases = sum(different_purchases.values())
    
    # Return the number of different purchases modulo 10007
    return total_different_purchases % 10007

if __name__ == '__main__':
    # Read the input
    N, C = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    Q = int(input())
    requirements_changes = []
    for _ in range(Q):
        requirements_changes.append(list(map(int, input().split())))
    
    # Calculate the number of purchases
    total_purchases = get_number_of_purchases(N, C, a, b)
    
    # Calculate the number of different purchases
    total_different_purchases = get_number_of_different_purchases(N, C, a, b, Q, requirements_changes)
    
    # Print the number of purchases and the number of different purchases
    print(total_purchases)
    print(total_different_purchases)

