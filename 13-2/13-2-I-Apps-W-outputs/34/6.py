
import math

def get_strength(army):
    # Sort the army in non-decreasing order
    army.sort()
    # Initialize the strength of the army to 0
    strength = 0
    # Iterate through the army and find the clans
    for i in range(len(army)):
        # Find the gcd of the current soldier and all previous soldiers in the clan
        gcd = army[i]
        for j in range(i):
            gcd = math.gcd(gcd, army[j])
        # Add the strength of the clan to the total strength
        strength += (i + 1) * gcd
    # Return the modulo of the strength
    return strength % 1000000007

