
def shortest_article_length(n, proofs):
    # Initialize a dictionary to store the number of words for each theorem
    num_words = {i: 0 for i in range(n)}
    # Iterate over the proofs
    for proof in proofs:
        # Get the length of the proof and the theorems it depends on
        length, num_theorems, *theorems = proof
        # Add the length of the proof to the total number of words for each theorem it depends on
        for theorem in theorems:
            num_words[theorem] += length
    # Return the minimum number of words needed to cover all theorems
    return min(num_words.values())

