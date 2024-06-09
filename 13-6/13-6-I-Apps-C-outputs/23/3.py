
def shortest_article(n, proofs):
    # Initialize a dictionary to store the number of words for each theorem
    theorem_words = {i: 0 for i in range(n)}

    # Iterate over the proofs and update the number of words for each theorem
    for proof in proofs:
        length, dependencies = proof[0], proof[1:]
        theorem_words[dependencies[0]] += length

    # Find the theorem with the minimum number of words
    min_words = min(theorem_words.values())

    # Return the minimum number of words
    return min_words

