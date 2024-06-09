
def get_min_light_radius(lanterns, street_length):
    lanterns.sort()
    max_distance = lanterns[-1] - lanterns[0]
    for i in range(1, len(lanterns)):
        distance = lanterns[i] - lanterns[i-1]
        if distance > max_distance:
            max_distance = distance
    return max_distance + 1

