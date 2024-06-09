
def get_optimal_probability(n, probabilities):
    probabilities.sort(reverse=True)
    optimal_probability = 0
    for i in range(n):
        optimal_probability += probabilities[i]
    return optimal_probability

