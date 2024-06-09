
def get_max_amount(n, A, B, C, T, messages):
    # Initialize the bank account and the number of unread messages
    bank_account = 0
    unread_messages = 0
    
    # Sort the messages by their arrival time
    messages.sort(key=lambda x: x[0])
    
    # Iterate through the messages
    for message in messages:
        # Get the arrival time and cost of the message
        arrival_time, cost = message
        
        # If the message has not been read yet, read it now
        if arrival_time <= T:
            # Update the bank account with the current cost of the message
            bank_account += cost
            
            # Update the number of unread messages
            unread_messages -= 1
            
            # Decrease the cost of the message by B each minute
            cost -= B
            
            # If the cost of the message has become negative, set it to 0
            if cost < 0:
                cost = 0
                
        # Update the bank account with the current number of unread messages
        bank_account += C * unread_messages
        
    return bank_account

