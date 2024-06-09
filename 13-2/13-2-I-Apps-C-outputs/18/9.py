
import sys

def solve(n, m, hints):
    # Initialize the answer sequence with all "false" answers
    answer_sequence = [0] * n

    # Iterate through the hints and update the answer sequence accordingly
    for hint in hints:
        l, r, same = hint
        for i in range(l-1, r):
            if same == "same":
                answer_sequence[i] = answer_sequence[l-1]
            else:
                answer_sequence[i] = 1 - answer_sequence[i]

    # Count the number of different answer sequences
    count = 0
    for i in range(1 << n):
        sequence = bin(i)[2:]
        sequence = "0" * (n - len(sequence)) + sequence
        valid = True
        for j in range(n):
            if sequence[j] != str(answer_sequence[j]):
                valid = False
                break
        if valid:
            count += 1

    return count % (10**9 + 7)

if __name__ == '__main__':
    n, m = map(int, input().split())
    hints = []
    for _ in range(m):
        l, r, same = input().split()
        hints.append((int(l), int(r), same))
    print(solve(n, m, hints))

