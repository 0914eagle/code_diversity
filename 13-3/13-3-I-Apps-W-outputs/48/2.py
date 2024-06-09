
def f1(n, b):
    # Function to check if the sequence is strictly increasing
    def is_strictly_increasing(seq):
        return all(seq[i] < seq[i+1] for i in range(len(seq)-1))

    # Function to find a permutation of the sequence that is strictly increasing
    def find_permutation(seq):
        permutation = list(seq)
        for i in range(len(seq)):
            for j in range(i+1, len(seq)):
                if permutation[i] < permutation[j]:
                    permutation[i], permutation[j] = permutation[j], permutation[i]
                    break
        return permutation

    # Check if the sequence is already strictly increasing
    if is_strictly_increasing(b):
        return b

    # Find a permutation of the sequence that is strictly increasing
    permutation = find_permutation(b)

    # Check if a permutation exists
    if permutation is None:
        return "No"

    return "Yes\n" + " ".join(str(x) for x in permutation)

def f2(n, b):
    # Function to check if the sequence is strictly increasing
    def is_strictly_increasing(seq):
        return all(seq[i] < seq[i+1] for i in range(len(seq)-1))

    # Function to find a permutation of the sequence that is strictly increasing
    def find_permutation(seq):
        permutation = list(seq)
        for i in range(len(seq)):
            for j in range(i+1, len(seq)):
                if permutation[i] < permutation[j]:
                    permutation[i], permutation[j] = permutation[j], permutation[i]
                    break
        return permutation

    # Check if the sequence is already strictly increasing
    if is_strictly_increasing(b):
        return b

    # Find a permutation of the sequence that is strictly increasing
    permutation = find_permutation(b)

    # Check if a permutation exists
    if permutation is None:
        return "No"

    return "Yes\n" + " ".join(str(x) for x in permutation)

if __name__ == '__main__':
    n = int(input())
    b = tuple(int(x) for x in input().split())
    print(f1(n, b))
    print(f2(n, b))

