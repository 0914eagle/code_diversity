
def get_cheapest_price(magnets):
    # Convert the magnets to integers
    magnets = [int(magnet) for magnet in magnets]
    
    # Sort the magnets in descending order
    magnets.sort(reverse=True)
    
    # Flip the first magnet if it is 6 or 9
    if magnets[0] in [6, 9]:
        magnets[0] = 10 - magnets[0]
    
    # Return the cheapest price formed by the magnets
    return int("".join(str(magnet) for magnet in magnets))

