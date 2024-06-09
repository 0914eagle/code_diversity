
def weightlifting_walrus(n, weights):
    weights.sort(reverse=True)
    total = 0
    for i in range(n):
        total += weights[i]
        if total >= 1000:
            return total
    return -1

