
def shortest_article(n, proofs):
    # Initialize a dictionary to store the length of each proof and the theorems it depends on
    proof_lengths = {}
    for proof in proofs:
        length, dependencies = proof
        proof_lengths[dependencies] = length

    # Initialize a set to store the theorems that have been proven
    proven_theorems = set()

    # Initialize the shortest article length
    shortest_length = 0

    # Loop through the theorems and find the shortest article length that proves them all
    for i in range(n):
        current_theorem = i
        while current_theorem not in proven_theorems:
            current_theorem_length = proof_lengths[current_theorem]
            proven_theorems.add(current_theorem)
            current_theorem = proof_lengths[current_theorem]
        shortest_length += current_theorem_length

    return shortest_length

