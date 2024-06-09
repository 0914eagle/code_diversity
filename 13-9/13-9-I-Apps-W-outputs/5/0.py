
def get_min_light_radius(lanterns, street_length):
    lanterns.sort()
    min_radius = 0
    for i in range(len(lanterns)):
        cur_radius = (lanterns[i] - min_radius) / 2
        if i == len(lanterns) - 1:
            break
        next_radius = (lanterns[i + 1] - lanterns[i]) / 2
        min_radius = max(cur_radius, next_radius)
    return min_radius

