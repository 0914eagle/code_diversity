
import sys

def solve(N, K):
    # Initialize the deque and the count of sequences
    deque = []
    count = 0
    
    # Insert the cards at the beginning or end of the deque
    for i in range(1, N+1):
        deque.append(i)
    
    # Perform the action N times
    for i in range(N):
        # Take out the card from the beginning or end of the deque and eat it
        card = deque.pop(0)
        
        # If the card is 1, increment the count
        if card == 1:
            count += 1
    
    # Return the count modulo 10^9 + 7
    return count % 1000000007

if __name__ == '__main__':
    N, K = map(int, input().split())
    print(solve(N, K))

