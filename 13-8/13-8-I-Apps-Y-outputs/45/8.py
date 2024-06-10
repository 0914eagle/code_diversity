
def get_diverse_garland(n, s):
    # Initialize the number of recolors to 0
    recolors = 0
    # Initialize the diverse garland as the input garland
    diverse_garland = s
    # Loop through the lamps in the garland
    for i in range(n - 1):
        # If the current lamp and the next lamp have the same color
        if s[i] == s[i + 1]:
            # Increment the number of recolors
            recolors += 1
            # Replace the color of the next lamp with the opposite color
            diverse_garland = diverse_garland[:i + 1] + "RGB"[s[i + 1] - "R"] + diverse_garland[i + 2:]
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

