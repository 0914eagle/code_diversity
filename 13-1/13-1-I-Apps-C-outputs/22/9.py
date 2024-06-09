
def f1(N, K):
    # Initialize the deque and the count of sequences
    deque = []
    count = 0
    
    # Loop through each card from 1 to N
    for card in range(1, N+1):
        # Insert the card at the beginning or end of the deque
        if card % 2 == 0:
            deque.append(card)
        else:
            deque.insert(0, card)
        
        # Eat the card from the beginning or end of the deque
        if card % 2 == 0:
            deque.pop()
        else:
            deque.pop(0)
        
        # If the K-th element is 1, increment the count
        if card == K:
            count += 1
    
    # Return the count modulo 10^9 + 7
    return count % 1000000007

