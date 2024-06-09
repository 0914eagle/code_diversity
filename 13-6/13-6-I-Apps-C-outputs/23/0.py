
def find_shortest_article_length(n, proofs):
    # Initialize a dictionary to store the number of words for each theorem
    theorem_words = {i: 0 for i in range(n)}

    # Iterate over the proofs and update the number of words for each theorem
    for proof in proofs:
        length, dependencies = proof[0], proof[1:]
        theorem_words[dependencies[0]] += length

    # Find the shortest length by finding the minimum number of words for Theorem 0
    return theorem_words[0]

