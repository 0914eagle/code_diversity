
def get_diverse_garland(n, s):
    # Initialize variables
    recolors = 0
    diverse_garland = s
    colors = ["R", "G", "B"]
    
    # Iterate through the garland and check if any two adjacent lamps have the same color
    for i in range(n - 1):
        if diverse_garland[i] == diverse_garland[i + 1]:
            # If they have the same color, find a new color for the lamp and replace it in the garland
            new_color = colors[0]
            if new_color == diverse_garland[i]:
                new_color = colors[1]
            diverse_garland = diverse_garland[:i] + new_color + diverse_garland[i + 1:]
            recolors += 1
    
    return recolors, diverse_garland

def main():
    n = int(input())
    s = input()
    recolors, diverse_garland = get_diverse_garland(n, s)
    print(recolors)
    print(diverse_garland)

if __name__ == '__main__':
    main()

