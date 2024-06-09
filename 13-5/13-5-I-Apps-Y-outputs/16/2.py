
def get_diverse_garland(n, s):
    # Initialize variables
    recolors = 0
    diverse_garland = []
    current_color = s[0]
    diverse_garland.append(current_color)
    
    # Iterate through the garland
    for i in range(1, n):
        # If the current color is different from the previous color, recolor it
        if s[i] != current_color:
            recolors += 1
            current_color = s[i]
        # Add the current color to the diverse garland
        diverse_garland.append(current_color)
    
    # Return the number of recolors and the diverse garland
    return recolors, "".join(diverse_garland)

def main():
    # Read the input
    n = int(input())
    s = input()
    
    # Call the function to get the diverse garland
    recolors, diverse_garland = get_diverse_garland(n, s)
    
    # Print the output
    print(recolors)
    print(diverse_garland)

if __name__ == '__main__':
    main()

