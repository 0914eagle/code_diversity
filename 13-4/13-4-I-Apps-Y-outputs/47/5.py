
def f1(n, s):
    # Calculate the number of regular bracket sequences of length 2n
    # containing the given bracket sequence s as a substring
    num_sequences = 0
    
    # Iterate over all possible positions of s in a regular bracket sequence
    for i in range(n - len(s) + 1):
        # Check if s is a substring of the regular bracket sequence
        if s in generate_sequence(2 * n, i):
            num_sequences += 1
    
    return num_sequences % 1000000007

def generate_sequence(n, i):
    # Generate all possible regular bracket sequences of length n
    if n == 0:
        return [""]
    elif n == 1:
        return ["()"]
    else:
        sequences = []
        for j in range(i, i + n - 1):
            for seq1 in generate_sequence(j, i):
                for seq2 in generate_sequence(n - j - 1, j + 1):
                    sequences.append("(" + seq1 + ")" + seq2)
        return sequences

if __name__ == '__main__':
    n = int(input())
    s = input()
    print(f1(n, s))

