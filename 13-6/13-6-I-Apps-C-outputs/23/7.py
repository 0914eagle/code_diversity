
def shortest_article_length(n, proofs):
    # Initialize a dictionary to store the number of words for each theorem
    num_words = {i: 0 for i in range(n)}
    # Initialize a list to store the dependencies of each theorem
    dependencies = [[] for _ in range(n)]

    # Loop through each proof and update the number of words and dependencies
    for proof in proofs:
        length, num_dep, *dep_list = proof
        num_words[num_dep] += length
        dependencies[num_dep].extend(dep_list)

    # Find the theorem with the fewest dependencies
    min_dep_count = min(map(len, dependencies))
    min_dep_theorems = [i for i, dep in enumerate(dependencies) if len(dep) == min_dep_count]

    # Return the sum of the number of words for the theorems with the fewest dependencies
    return sum(num_words[i] for i in min_dep_theorems)

