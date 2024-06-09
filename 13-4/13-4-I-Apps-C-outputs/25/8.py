
def get_probability(n, probabilities):
    probabilities.sort(reverse=True)
    total = 0
    for i in range(n):
        total += probabilities[i]
    return total

