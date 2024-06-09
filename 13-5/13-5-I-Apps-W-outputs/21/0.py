
def wallace_the_weightlifting_walrus(n, weights):
    weights.sort()
    total = 0
    for i in range(n):
        total += weights[i]
        if total >= 1000:
            break
    if total == 1000:
        return total
    elif total > 1000:
        return total - weights[i]
    else:
        return total + weights[i]

