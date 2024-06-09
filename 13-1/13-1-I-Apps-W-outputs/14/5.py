
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
    
    # Return the maximum bank account amount after T minutes
    return bank_account + unread_messages * C * T

def main():
    n, A, B, C, T = map(int, input().split())
    t = list(map(int, input().split()))
    print(get_max_bank_account(n, A, B, C, T, t))

if __name__ == '__main__':
    main()

