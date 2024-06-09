
def get_max_bank_account(n, A, B, C, T, messages):
    # Initialize the bank account and the number of unread messages
    bank_account = 0
    unread_messages = 0
    
    # Sort the messages by their arrival time
    messages.sort(key=lambda x: x[0])
    
    # Iterate through the messages
    for message in messages:
        # Calculate the current cost of the message
        current_cost = A - B * (T - message[0])
        
        # If the message is received before T minutes, add it to the bank account
        if message[0] <= T:
            bank_account += current_cost
        
        # If the message is received after T minutes, add it to the number of unread messages
        else:
            unread_messages += 1
    
    # Return the maximum bank account value
    return bank_account + C * unread_messages

def main():
    n, A, B, C, T = map(int, input().split())
    messages = []
    for _ in range(n):
        messages.append(list(map(int, input().split())))
    print(get_max_bank_account(n, A, B, C, T, messages))

if __name__ == '__main__':
    main()

