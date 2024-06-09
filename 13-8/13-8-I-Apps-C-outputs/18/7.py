
def solve(d, t, c, r, clouds, roofs):
    # Initialize variables
    total_rain = 0
    current_time = 0
    current_roof = 0

    # Sort the clouds by their starting time
    clouds.sort(key=lambda x: x[0])

    # Loop through the clouds
    for cloud in clouds:
        s, e, p, a = cloud

        # Check if the cloud is in your zip code
        if p > 0:
            # Check if the cloud is currently raining
            if current_time >= s and current_time < e:
                # Add the rain amount to the total
                total_rain += a

                # Check if the cloud is over a roof
                while current_roof < len(roofs) and roofs[current_roof][0] <= s:
                    current_roof += 1

                # Check if the cloud is under a roof
                while current_roof > 0 and roofs[current_roof - 1][1] > e:
                    current_roof -= 1

    # Return the total rain amount
    return total_rain

