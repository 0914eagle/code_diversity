
def f1(N, K):
    # Initialize the deque and the count of sequences
    deque = []
    count = 0
    
    # Loop through each card from 1 to N
    for card in range(1, N+1):
        # Insert the card at the beginning or end of the deque
        deque.append(card)
        deque.append(card)
        
        # Eat the card from the beginning or end of the deque
        deque.pop(0)
        deque.pop()
        
        # If the K-th element is 1, increment the count
        if deque[K-1] == 1:
            count += 1
    
    # Return the count modulo 10^9 + 7
    return count % 1000000007

