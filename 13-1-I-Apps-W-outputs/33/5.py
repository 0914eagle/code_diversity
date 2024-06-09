
def num_tilings(w, h):
    # Initialize the number of tilings to 0
    num_tilings = 0
    
    # Loop through all possible rotations of the tile
    for i in range(4):
        # Calculate the number of tilings for the current rotation
        num_tilings += num_tilings_helper(w, h, i)
    
    # Return the number of tilings modulo 998244353
    return num_tilings % 998244353

def num_tilings_helper(w, h, rotation):
    # Base case: if the kitchen is 1x1, there is only one way to tile it
    if w == 1 and h == 1:
        return 1
    
    # Initialize the number of tilings to 0
    num_tilings = 0
    
    # Loop through all possible ways to tile the floor
    for i in range(w):
        for j in range(h):
            # Calculate the number of tilings for the current tile placement
            num_tilings += num_tilings_helper(w-i-1, h-j-1, (rotation+1)%4)
    
    # Return the number of tilings
    return num_tilings

