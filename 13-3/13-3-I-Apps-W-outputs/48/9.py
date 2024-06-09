
def f1(n, b):
    # Function to check if the sequence is strictly increasing
    def is_strictly_increasing(seq):
        return all(seq[i] < seq[i+1] for i in range(len(seq)-1))

    # Function to find a permutation of the sequence that is strictly increasing
    def find_permutation(seq):
        permutation = []
        for i in range(n):
            # Find the smallest element in the sequence that is greater than the last element in the permutation
            smallest = min(seq, key=lambda x: x if x > permutation[-1] else float('inf'))
            permutation.append(smallest)
            seq.remove(smallest)
        return permutation

    # Check if the given sequence is strictly increasing
    if is_strictly_increasing(b):
        return "Yes\n" + " ".join(map(str, b))

    # Find a permutation of the sequence that is strictly increasing
    permutation = find_permutation(b)

    # Check if a permutation exists
    if permutation:
        return "Yes\n" + " ".join(map(str, permutation))
    else:
        return "No"

def f2(...):
    # Function to check if the sequence is strictly increasing
    def is_strictly_increasing(seq):
        return all(seq[i] < seq[i+1] for i in range(len(seq)-1))

    # Function to find a permutation of the sequence that is strictly increasing
    def find_permutation(seq):
        permutation = []
        for i in range(n):
            # Find the smallest element in the sequence that is greater than the last element in the permutation
            smallest = min(seq, key=lambda x: x if x > permutation[-1] else float('inf'))
            permutation.append(smallest)
            seq.remove(smallest)
        return permutation

    # Check if the given sequence is strictly increasing
    if is_strictly_increasing(b):
        return "Yes\n" + " ".join(map(str, b))

    # Find a permutation of the sequence that is strictly increasing
    permutation = find_permutation(b)

    # Check if a permutation exists
    if permutation:
        return "Yes\n" + " ".join(map(str, permutation))
    else:
        return "No"

if __name__ == '__main__':
    n = int(input())
    b = list(map(int, input().split()))
    print(f1(n, b))

