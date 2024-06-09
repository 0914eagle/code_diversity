
import sys

def solve(N, K):
    # Initialize the deque and the sequence
    deque = []
    sequence = []

    # Insert the cards at the beginning or the end of the deque one at a time, in order from 1 to N
    for i in range(1, N+1):
        if i % 2 == 1:
            deque.append(i)
        else:
            deque.insert(0, i)

    # Eat the card from the beginning or the end of the deque and add it to the sequence
    for i in range(N):
        if i % 2 == 0:
            sequence.append(deque.pop(0))
        else:
            sequence.append(deque.pop())

    # Count the number of sequences that have a 1 in the K-th position
    count = 0
    for seq in sequence:
        if seq[K-1] == 1:
            count += 1

    return count % (10**9 + 7)

if __name__ == "__main__":
    N, K = map(int, input().split())
    print(solve(N, K))

