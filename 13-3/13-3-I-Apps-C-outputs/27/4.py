
import sys

def solve(N, K):
    # Initialize the deque and the count of sequences
    deque = []
    count = 0
    
    # Insert the cards at the beginning or end of the deque
    for i in range(1, N+1):
        if i % 2 == 1:
            deque.append(i)
        else:
            deque.insert(0, i)
    
    # Eat the cards and count the sequences
    while deque:
        card = deque.pop(0)
        if card == K:
            count += 1
    
    return count % (10**9 + 7)

if __name__ == '__main__':
    N, K = map(int, input().split())
    print(solve(N, K))

