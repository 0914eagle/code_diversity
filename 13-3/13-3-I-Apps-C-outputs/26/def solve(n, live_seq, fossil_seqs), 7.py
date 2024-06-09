
def solve(n, live_seq, fossil_seqs):
    # Initialize variables
    first_path = []
    second_path = []
    impossible = False

    # Iterate through the fossil sequences
    for seq in fossil_seqs:
        # Check if the sequence is in the genetic history of the live species
        if seq in live_seq:
            # If it is, add it to the first path
            first_path.append(seq)
        else:
            # If it is not, add it to the second path
            second_path.append(seq)

    # Check if it is possible to have two evolutionary paths
    if len(first_path) == 0 or len(second_path) == 0:
        impossible = True

    # Return the results
    if impossible:
        return "impossible"
    else:
        return str(len(first_path)) + " " + str(len(second_path)) + "\n" + "\n".join(first_path) + "\n" + "\n".join(second_path)

