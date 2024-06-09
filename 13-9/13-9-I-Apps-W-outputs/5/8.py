
def get_min_light_radius(lanterns, street_length):
    lanterns.sort()
    max_distance = 0
    for i in range(len(lanterns) - 1):
        distance = lanterns[i + 1] - lanterns[i]
        max_distance = max(max_distance, distance)
    return max_distance

