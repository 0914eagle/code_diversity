
def get_rain_amount(d, t, c, r):
    # Initialize variables
    rain_amount = 0
    current_time = 0
    roof_segments = []

    # Read the clouds and roof segments
    for i in range(c):
        s, e, p, a = map(int, input().split())
        rain_amount += p * a * (e - s)

    for i in range(r):
        x, y = map(int, input().split())
        roof_segments.append((x, y))

    # Sort the roof segments by their start position
    roof_segments.sort(key=lambda x: x[0])

    # Loop through the clouds and check for overlap with the roof segments
    for s, e, p, a in clouds:
        # Check if the cloud is currently raining
        if current_time >= s and current_time < e:
            # Check if the cloud is under a roof
            under_roof = False
            for x, y in roof_segments:
                if x <= current_time and current_time < y:
                    under_roof = True
                    break

            # If the cloud is not under a roof, add its rainfall amount to the total
            if not under_roof:
                rain_amount += a

        # Update the current time
        current_time = e

    return rain_amount

