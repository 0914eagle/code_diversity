
def get_suitable_colorings(n, k):
    # Initialize a list to store the results
    results = []
    
    # Iterate over all possible colorings
    for i in range(2**(n*n)):
        # Convert the integer to a binary string
        binary_string = bin(i)[2:]
        binary_string = binary_string.zfill(n*n)
        
        # Check if the coloring is suitable
        if is_suitable(binary_string, n, k):
            # Add the coloring to the results list
            results.append(binary_string)
    
    # Return the number of suitable colorings modulo 998244353
    return len(results) % 998244353

def is_suitable(coloring, n, k):
    # Check if the coloring is beautiful
    if not is_beautiful(coloring, n):
        return False
    
    # Check if the coloring includes a rectangle of a single color
    for i in range(n):
        for j in range(n):
            # Check if the current tile is the same as the top-left tile
            if coloring[i*n+j] != coloring[0]:
                # Check if the current tile is the same as the top-right tile
                if coloring[i*n+j] != coloring[n-1]:
                    # Check if the current tile is the same as the bottom-left tile
                    if coloring[i*n+j] != coloring[(n-1)*n]:
                        # Check if the current tile is the same as the bottom-right tile
                        if coloring[i*n+j] != coloring[(n-1)*n+n-1]:
                            # Check if the current tile is the same as the top-left tile
                            if coloring[i*n+j] != coloring[0]:
                                # Check if the current tile is the same as the top-right tile
                                if coloring[i*n+j] != coloring[n-1]:
                                    # Check if the current tile is the same as the bottom-left tile
                                    if coloring[i*n+j] != coloring[(n-1)*n]:
                                        # Check if the current tile is the same as the bottom-right tile
                                        if coloring[i*n+j] != coloring[(n-1)*n+n-1]:
                                            # If the coloring includes a rectangle of a single color, return False
                                            return False
    
    # If the coloring is not suitable, return False
    return True

def is_beautiful(coloring, n):
    # Check if the coloring is beautiful
    for i in range(n):
        for j in range(n):
            # Check if the current tile is the same as the top-left tile
            if coloring[i*n+j] != coloring[0]:
                # Check if the current tile is the same as the top-right tile
                if coloring[i*n+j] != coloring[n-1]:
                    # Check if the current tile is the same as the bottom-left tile
                    if coloring[i*n+j] != coloring[(n-1)*n]:
                        # Check if the current tile is the same as the bottom-right tile
                        if coloring[i*n+j] != coloring[(n-1)*n+n-1]:
                            # If the coloring is not beautiful, return False
                            return False
    
    # If the coloring is beautiful, return True
    return True

if __name__ == '__main__':
    n, k = map(int, input().split())
    print(get_suitable_colorings(n, k))

