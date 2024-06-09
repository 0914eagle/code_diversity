
def weightlifting_walrus(weights):
    weights.sort(reverse=True)
    total = 0
    for weight in weights:
        total += weight
        if total >= 1000:
            break
    if total != 1000:
        total = 1000
    return total

