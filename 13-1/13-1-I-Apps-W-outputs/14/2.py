
def get_max_bank_account(n, A, B, C, T, t):
    # Initialize the bank account and the number of unread messages
    bank_account = 0
    unread_messages = 0
    
    # Loop through each message and its arrival time
    for i in range(n):
        # Calculate the cost of the message after T minutes
        cost = A - B * min(T, t[i])
        
        # If the message is read before T minutes, add its cost to the bank account
        if t[i] <= T:
            bank_account += cost
        
        # If the message is read after T minutes, add its cost to the bank account and also add the cost of the unread messages
        else:
            bank_account += cost + C * unread_messages
            unread_messages += 1
    
    # Return the maximum bank account amount
    return bank_account

