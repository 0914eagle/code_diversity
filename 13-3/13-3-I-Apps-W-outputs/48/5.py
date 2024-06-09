
def f1(n, b):
    # Function to check if the sequence is strictly increasing
    def is_strictly_increasing(seq):
        return all(seq[i] < seq[i+1] for i in range(len(seq)-1))

    # Function to find all permutations of a list
    def find_permutations(seq):
        if len(seq) == 1:
            return [seq]
        permutations = []
        for i in range(len(seq)):
            remaining = seq[:i] + seq[i+1:]
            for p in find_permutations(remaining):
                permutations.append([seq[i]] + p)
        return permutations

    # Function to check if a permutation is valid
    def is_valid_permutation(permutation):
        # Check if the permutation is a permutation of the original sequence
        if len(permutation) != len(set(permutation)):
            return False
        # Check if the permutation leads to a strictly increasing sequence
        return is_strictly_increasing(permutation)

    # Find all permutations of the input sequence
    permutations = find_permutations(b)

    # Check if any permutation is valid
    for permutation in permutations:
        if is_valid_permutation(permutation):
            return permutation

    # If no permutation is valid, return "No"
    return "No"

def f2(n, b):
    # Function to find the next element in the sequence
    def next_element(seq):
        return seq[0] ^ seq[1]

    # Function to check if the sequence is strictly increasing
    def is_strictly_increasing(seq):
        return all(seq[i] < seq[i+1] for i in range(len(seq)-1))

    # Function to find all permutations of a list
    def find_permutations(seq):
        if len(seq) == 1:
            return [seq]
        permutations = []
        for i in range(len(seq)):
            remaining = seq[:i] + seq[i+1:]
            for p in find_permutations(remaining):
                permutations.append([seq[i]] + p)
        return permutations

    # Function to check if a permutation is valid
    def is_valid_permutation(permutation):
        # Check if the permutation is a permutation of the original sequence
        if len(permutation) != len(set(permutation)):
            return False
        # Check if the permutation leads to a strictly increasing sequence
        return is_strictly_increasing(permutation)

    # Find all permutations of the input sequence
    permutations = find_permutations(b)

    # Check if any permutation is valid
    for permutation in permutations:
        if is_valid_permutation(permutation):
            return permutation

    # If no permutation is valid, return "No"
    return "No"

if __name__ == '__main__':
    n = int(input())
    b = list(map(int, input().split()))
    print(f1(n, b))
    print(f2(n, b))

