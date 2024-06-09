
def find_closest_weight(weights, target):
    return min(weights, key=lambda x: abs(x - target))

