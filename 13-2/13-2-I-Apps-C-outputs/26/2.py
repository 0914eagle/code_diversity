
def f1(n, live_seq, fossil_seqs):
    # Initialize variables
    first_path = []
    second_path = []
    visited = set()

    # Add the live sequence to the first path
    first_path.append(live_seq)
    visited.add(live_seq)

    # Iterate through the fossil sequences
    for seq in fossil_seqs:
        # If the sequence is not in the visited set, add it to the first path
        if seq not in visited:
            first_path.append(seq)
            visited.add(seq)
        # If the sequence is already in the visited set, add it to the second path
        else:
            second_path.append(seq)

    # Return the first path and the second path
    return first_path, second_path

def f2(n, live_seq, fossil_seqs):
    # Initialize variables
    first_path = []
    second_path = []
    visited = set()

    # Add the live sequence to the first path
    first_path.append(live_seq)
    visited.add(live_seq)

    # Iterate through the fossil sequences
    for seq in fossil_seqs:
        # If the sequence is not in the visited set, add it to the first path
        if seq not in visited:
            first_path.append(seq)
            visited.add(seq)
        # If the sequence is already in the visited set, add it to the second path
        else:
            second_path.append(seq)

    # Return the first path and the second path
    return first_path, second_path

if __name__ == '__main__':
    n = int(input())
    live_seq = input()
    fossil_seqs = [input() for _ in range(n)]
    first_path, second_path = f1(n, live_seq, fossil_seqs)
    print(len(first_path), len(second_path))
    for seq in first_path:
        print(seq)
    for seq in second_path:
        print(seq)

