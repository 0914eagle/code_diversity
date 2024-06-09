
def f1(N, K):
    # Initialize the deque and the sequence
    deque = []
    sequence = []
    
    # Insert the cards at the beginning or the end of the deque
    for i in range(1, N+1):
        if i % 2 == 0:
            deque.append(i)
        else:
            deque.insert(0, i)
    
    # Eat the cards from the beginning or the end of the deque
    for i in range(N):
        if i % 2 == 0:
            sequence.append(deque.pop(0))
        else:
            sequence.append(deque.pop())
    
    # Count the number of sequences that have K-th element as 1
    count = 0
    for seq in sequence:
        if seq[K-1] == 1:
            count += 1
    
    return count % (10**9 + 7)

