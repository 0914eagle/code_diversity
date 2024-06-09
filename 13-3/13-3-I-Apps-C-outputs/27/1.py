
import sys

def solve(N, K):
    # Initialize the deque with the numbers 1 to N
    deque = list(range(1, N+1))
    
    # Initialize the count of sequences with K-th element as 1 to 0
    count = 0
    
    # Loop through each card and eat it
    for i in range(N):
        # Eat the card at the beginning of the deque
        card = deque.pop(0)
        
        # If the card is 1, increment the count
        if card == K:
            count += 1
        
        # Insert the card at the end of the deque
        deque.append(card)
    
    # Return the count modulo 10^9 + 7
    return count % (10**9 + 7)

if __name__ == "__main__":
    N, K = map(int, input().split())
    print(solve(N, K))

