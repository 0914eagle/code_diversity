
def f1(n, bracket_sequences):
    # Your code here
    return max_pairs

def f2(n, bracket_sequences):
    # Your code here
    return max_pairs

if __name__ == '__main__':
    n = int(input())
    bracket_sequences = []
    for _ in range(n):
        bracket_sequences.append(input())
    max_pairs = f1(n, bracket_sequences)
    print(max_pairs)

