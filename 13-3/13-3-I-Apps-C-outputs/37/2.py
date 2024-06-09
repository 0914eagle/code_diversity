
def f1(n, *magnets):
    # Convert the magnets to integers
    magnets = [int(''.join(str(magnet))) for magnet in magnets]
    
    # Find the smallest magnet
    smallest = min(magnets)
    
    # Find the index of the smallest magnet
    smallest_index = magnets.index(smallest)
    
    # Move the smallest magnet to the front
    magnets.insert(0, magnets.pop(smallest_index))
    
    # Return the rearranged magnets
    return ''.join(str(magnet) for magnet in magnets)

