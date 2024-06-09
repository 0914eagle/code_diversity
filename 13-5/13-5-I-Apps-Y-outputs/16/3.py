
def get_diverse_garland(n, s):
    # Initialize the number of recolors to 0
    recolors = 0
    
    # Initialize the diverse garland as the initial garland
    diverse_garland = s
    
    # Iterate through the garland
    for i in range(n - 1):
        # If the current and next lamp have the same color
        if s[i] == s[i + 1]:
            # Recolor the next lamp to the opposite color
            diverse_garland = diverse_garland[:i + 1] + "R" if s[i] == "G" else "G"
            recolors += 1
    
    # Return the number of recolors and the diverse garland
    return recolors, diverse_garland

def main():
    # Read the input
    n = int(input())
    s = input()
    
    # Call the function to get the diverse garland
    recolors, diverse_garland = get_diverse_garland(n, s)
    
    # Print the number of recolors and the diverse garland
    print(recolors)
    print(diverse_garland)

if __name__ == '__main__':
    main()

