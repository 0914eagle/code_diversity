
import sys

def solve(n, m, hints):
    # Initialize the answer sequence with all "false" answers
    answer_sequence = [False] * n

    # Iterate through the hints and update the answer sequence accordingly
    for hint in hints:
        l, r, same = hint
        for i in range(l, r + 1):
            if same == "same":
                answer_sequence[i] = answer_sequence[l]
            else:
                answer_sequence[i] = not answer_sequence[l]

    # Count the number of different answer sequences
    num_sequences = 0
    for i in range(1 << n):
        sequence = []
        for j in range(n):
            if i & (1 << j):
                sequence.append(True)
            else:
                sequence.append(False)
        if all(sequence[l] == sequence[r] for l, r in hints):
            num_sequences += 1

    return num_sequences % (10**9 + 7)

if __name__ == '__main__':
    n, m = map(int, input().split())
    hints = []
    for _ in range(m):
        l, r, same = input().split()
        hints.append((int(l), int(r), same))
    print(solve(n, m, hints))

