
import sys

def solve(N, K):
    # Initialize the deque and the sequence
    deque = []
    sequence = []

    # Insert the cards at the beginning or the end of the deque one at a time, in order from 1 to N
    for i in range(1, N+1):
        deque.append(i)

    # Perform the action N times: take out the card from the beginning or the end of the deque and eat it
    for i in range(N):
        # Take out the card from the beginning or the end of the deque
        card = deque.pop(0)

        # Add the card to the sequence
        sequence.append(card)

    # Count the number of sequences that satisfy the condition
    count = 0
    for i in range(len(sequence)):
        if sequence[i] == K:
            count += 1

    # Return the result modulo 10^9 + 7
    return count % 1000000007

if __name__ == "__main__":
    N, K = map(int, input().split())
    print(solve(N, K))

