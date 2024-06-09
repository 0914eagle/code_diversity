
def solve(A, B, C, D, E, F):
    # Calculate the maximum amount of sugar that can be dissolved in water
    max_sugar = E * 100 / A

    # Initialize the mass of sugar and water to 0
    sugar, water = 0, 0

    # Loop until the mass of sugar and water is less than or equal to the maximum amount that can be contained in the beaker
    while sugar + water <= F:
        # If the current mass of sugar is less than or equal to the maximum amount that can be dissolved in water, add 100 grams of water
        if sugar <= max_sugar:
            water += 100
        # If the current mass of sugar is greater than the maximum amount that can be dissolved in water, add as much sugar as possible
        else:
            sugar += max_sugar

        # If the current mass of sugar is less than or equal to C, add C grams of sugar
        if sugar <= C:
            sugar += C
        # If the current mass of sugar is greater than C but less than or equal to D, add D grams of sugar
        elif sugar <= D:
            sugar += D
        # If the current mass of sugar is greater than D, do not add any sugar

    # Return the mass of sugar and water
    return sugar, water

