
def solve(d, t, c, r, clouds, roofs):
    # Initialize variables
    total_rain = 0
    current_time = 0
    on_roof = False

    # Sort clouds by starting time
    clouds.sort(key=lambda x: x[0])

    # Iterate through clouds
    for cloud in clouds:
        s, e, p, a = cloud
        current_time = max(current_time, s)
        if current_time <= t:
            # Check if cloud is in zip code
            if p > 0:
                # Check if cloud is on roof
                if on_roof:
                    # Cloud is on roof, reduce rain intensity by half
                    total_rain += a / 2
                else:
                    # Cloud is not on roof, add full rain intensity
                    total_rain += a
        current_time = e

    # Check if there are any remaining roof segments
    if r > 0:
        # Sort roof segments by starting position
        roofs.sort(key=lambda x: x[0])
        # Iterate through roof segments
        for roof in roofs:
            x, y = roof
            if x <= d and y > d:
                # Roof segment is over home and the bus stop, set on_roof to True
                on_roof = True
            elif x > d and y <= d:
                # Roof segment is between home and the bus stop, set on_roof to False
                on_roof = False
            elif x <= d and y <= d:
                # Roof segment is over home and the bus stop, set on_roof to True
                on_roof = True
            elif x > d and y > d:
                # Roof segment is between home and the bus stop, set on_roof to False
                on_roof = False

    # Return total rain
    return total_rain

