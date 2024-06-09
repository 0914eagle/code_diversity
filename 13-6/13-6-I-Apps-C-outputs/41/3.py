
def get_number_of_purchases(N, C, a, b, Q, requirements_changes):
    # Initialize a dictionary to store the number of purchases for each client
    purchases = {}
    for i in range(N):
        purchases[i+1] = [0, 0]
    
    # Loop through the requirements changes
    for requirement_change in requirements_changes:
        P, a_P, b_P = requirement_change
        # Update the number of purchases for client P
        purchases[P][0] = a_P
        purchases[P][1] = b_P
    
    # Loop through the clients and calculate the number of purchases
    total_purchases = 0
    for client, purchases in purchases.items():
        total_purchases += max(purchases)
    
    # Return the number of purchases modulo 10007
    return total_purchases % 10007

