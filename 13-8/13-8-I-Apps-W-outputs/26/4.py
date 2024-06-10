
def align_maps(map1, map2):
    # Find the size of the common section
    m = len(map1[0])
    n = len(map2)
    
    # Initialize the result
    result = []
    
    # Iterate over the rows of the first map
    for i in range(len(map1)):
        # Iterate over the columns of the second map
        for j in range(n):
            # Check if the section of size m x m in the first map starting at row i and column j is equal to the section of the second map starting at row j and column i
            if map1[i][j:j+m] == map2[j][i:i+m]:
                # If it is, add the indices to the result
                result.append([i+1, j+1])
    
    # Return the result
    return result

def main():
    # Read the input
    n, m = map(int, input().split())
    map1 = [input() for _ in range(n)]
    map2 = [input() for _ in range(m)]
    
    # Align the maps
    result = align_maps(map1, map2)
    
    # Print the result
    print(" ".join(map(str, result[0])))

if __name__ == '__main__':
    main()

