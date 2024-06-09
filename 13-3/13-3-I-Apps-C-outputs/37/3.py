
def f1(n, *magnets):
    # Convert the magnets to integers
    magnets = [int(''.join(str(digit) for digit in magnet)) for magnet in magnets]
    
    # Find the smallest number that can be formed by rearranging the magnets
    smallest = min(int(''.join(str(digit) for digit in magnets)) for magnets in permutations(magnets))
    
    # Return the smallest number
    return smallest

