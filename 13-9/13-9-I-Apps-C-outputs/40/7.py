
def get_max_earnings(gemstones):
    # Initialize a dictionary to store the earnings for each gemstone
    earnings = {}
    for i, a in enumerate(gemstones, start=1):
        earnings[i] = a

    # Iterate through the gemstones and find the maximum earning by smashing the gems with multiples of x
    for x in range(1, len(gemstones)+1):
        for i in range(x, len(gemstones)+1, x):
            if i in earnings:
                earnings[i] = max(earnings[i], earnings[i-x] + earnings[i])

    # Return the maximum earning
    return max(earnings.values())

