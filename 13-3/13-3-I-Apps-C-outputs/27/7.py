
import sys

def solve(N, K):
    # Initialize the deque and the sequence
    deque = []
    sequence = []

    # Insert the cards at the beginning or the end of the deque
    for i in range(1, N+1):
        if i % 2 == 1:
            deque.append(i)
        else:
            deque.insert(0, i)

    # Eat the cards and construct the sequence
    for i in range(N):
        card = deque.pop(0)
        sequence.append(card)
        if card == K:
            break

    # Count the number of sequences that satisfy the condition
    count = 0
    for perm in permutations(sequence):
        if perm[K-1] == 1:
            count += 1

    return count % (10**9 + 7)

if __name__ == '__main__':
    N, K = map(int, input().split())
    print(solve(N, K))

