
def get_diverse_garland(n, s):
    # Initialize the number of recolors to 0
    recolors = 0
    
    # Initialize the diverse garland as the initial garland
    diverse_garland = s
    
    # Iterate through the garland
    for i in range(n - 1):
        # If the current and next lamp have the same color
        if s[i] == s[i + 1]:
            # Increment the number of recolors
            recolors += 1
            # Change the color of the next lamp to the opposite color
            diverse_garland = diverse_garland[:i + 1] + "R" if s[i] == "G" else "G"
            diverse_garland = diverse_garland[:i + 2] + "B" if s[i] == "R" else "R"
    
    # Return the number of recolors and the diverse garland
    return recolors, diverse_garland

def main():
    n = int(input())
    s = input()
    recolors, diverse_garland = get_diverse_garland(n, s)
    print(recolors)
    print(diverse_garland)

if __name__ == '__main__':
    main()

