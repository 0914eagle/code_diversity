
def shortest_article_length(n, proofs):
    # Initialize a dictionary to store the length of each proof and the number of theorems it depends on
    proof_lengths = {}
    for proof in proofs:
        l, k, *d = proof
        proof_lengths[l] = k

    # Initialize a set to store the theorems that have been proven
    proven_theorems = set()

    # Initialize the shortest article length
    shortest_length = 0

    # Iterate through the proofs in order of length
    for l in sorted(proof_lengths):
        # If the current proof depends on any theorems that have not been proven, skip it
        if proof_lengths[l] - len(proven_theorems) > 0:
            continue

        # If the current proof depends on any theorems that have been proven, add its length to the shortest article length
        shortest_length += l

        # Add the current theorem to the set of proven theorems
        proven_theorems.add(l)

    return shortest_length

