
def get_min_heaters(n, r, a):
    # Sort the heaters in ascending order
    sorted_heaters = sorted(a)

    # Initialize the minimum number of heaters needed to warm up the whole house
    min_heaters = 0

    # Iterate through the heaters and count the number of heaters needed to warm up each element
    for i in range(n):
        # Find the closest heater to the current element
        closest_heater = sorted_heaters[0]
        for j in range(1, len(sorted_heaters)):
            if abs(sorted_heaters[j] - i) < abs(closest_heater - i):
                closest_heater = sorted_heaters[j]

        # If the current element is not warmed up by any heater, increment the minimum number of heaters needed
        if closest_heater - r + 1 > i or closest_heater + r - 1 < i:
            min_heaters += 1

    return min_heaters

