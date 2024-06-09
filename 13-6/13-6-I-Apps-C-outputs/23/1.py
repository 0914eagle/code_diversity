
def shortest_article(n, proofs):
    # Initialize a dictionary to store the number of words for each theorem
    num_words = {i: 0 for i in range(n)}
    # Iterate over the proofs
    for proof in proofs:
        # Get the length of the current proof
        length = proof[0]
        # Get the list of theorems the current proof depends on
        theorems = proof[1:]
        # Update the number of words for each theorem the current proof depends on
        for theorem in theorems:
            num_words[theorem] += length
    # Find the minimum number of words for Theorem 0
    min_words = num_words[0]
    # Return the minimum number of words
    return min_words

