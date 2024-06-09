
def shortest_article(n, proofs):
    # Initialize a dictionary to store the number of words for each theorem
    num_words = {i: 0 for i in range(n)}
    # Iterate over the proofs
    for proof in proofs:
        # Get the length of the proof and the number of theorems it depends on
        length, num_theorems = proof[:2]
        # Get the numbers of the theorems the proof depends on
        theorems = proof[2:]
        # Add the length of the proof to the number of words for each dependent theorem
        for theorem in theorems:
            num_words[theorem] += length
    # Return the minimum number of words needed to cover Theorem 0
    return min(num_words[0], *num_words.values())

