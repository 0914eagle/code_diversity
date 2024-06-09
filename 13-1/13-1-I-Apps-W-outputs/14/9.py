
def get_max_bank_account(n, A, B, C, T, t):
    # Initialize the bank account and the number of unread messages
    bank_account = 0
    unread_messages = 0
    
    # Loop through each message and its arrival time
    for i in range(n):
        # Calculate the cost of the message after T minutes
        cost = A - B * min(T, t[i])
        
        # If the message is received before T minutes, add it to the bank account
        if t[i] <= T:
            bank_account += cost
        
        # If the message is received after T minutes, add it to the number of unread messages
        else:
            unread_messages += 1
    
    # Calculate the total amount of money earned from unread messages
    total_unread_messages = unread_messages * C * T
    
    # Return the maximum amount of money that can be held in the bank account
    return bank_account + total_unread_messages

