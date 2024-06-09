
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
    answer_sequences = set()
    for i in range(2**n):
        answer_sequence = []
        for j in range(n):
            if i & (1 << j):
                answer_sequence.append(True)
            else:
                answer_sequence.append(False)
        answer_sequences.add(tuple(answer_sequence))

    return len(answer_sequences) % (10**9 + 7)

if __name__ == '__main__':
    n, m = map(int, input().split())
    hints = []
    for _ in range(m):
        l, r, same = input().split()
        hints.append((int(l), int(r), same))
    print(solve(n, m, hints))

