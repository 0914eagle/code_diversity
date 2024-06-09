
def get_diverse_garland(n, s):
    # Initialize the number of recolors needed
    recolors = 0
    
    # Initialize the diverse garland
    diverse_garland = []
    
    # Iterate through the initial garland
    for i in range(n):
        # If the current lamp is red and the next lamp is also red, recolor it to green
        if s[i] == "R" and (i == n-1 or s[i+1] == "R"):
            diverse_garland.append("G")
            recolors += 1
        # If the current lamp is green and the next lamp is also green, recolor it to blue
        elif s[i] == "G" and (i == n-1 or s[i+1] == "G"):
            diverse_garland.append("B")
            recolors += 1
        # If the current lamp is blue and the next lamp is also blue, recolor it to red
        elif s[i] == "B" and (i == n-1 or s[i+1] == "B"):
            diverse_garland.append("R")
            recolors += 1
        # If the current lamp is not red, green or blue, recolor it to red
        else:
            diverse_garland.append("R")
            recolors += 1
    
    # Return the number of recolors needed and the diverse garland
    return recolors, "".join(diverse_garland)

def main():
    n = int(input())
    s = input()
    recolors, diverse_garland = get_diverse_garland(n, s)
    print(recolors)
    print(diverse_garland)

if __name__ == '__main__':
    main()

