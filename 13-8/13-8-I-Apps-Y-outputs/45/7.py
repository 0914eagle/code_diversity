
def get_diverse_garland(n, s):
    # Initialize a dictionary to store the number of recolors needed for each color
    recolors = {"R": 0, "G": 0, "B": 0}
    
    # Iterate through the garland and count the number of recolors needed for each color
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            recolors[s[i]] += 1
    
    # Find the color with the minimum number of recolors needed
    min_recolors = min(recolors.values())
    
    # Initialize a list to store the diverse garland
    diverse_garland = []
    
    # Iterate through the garland and recolor the lamps with the minimum number of recolors needed
    for i in range(n):
        if recolors[s[i]] == min_recolors:
            diverse_garland.append(s[i])
        else:
            diverse_garland.append("R" if s[i] == "G" else "G")
    
    return diverse_garland

def main():
    n = int(input())
    s = input()
    diverse_garland = get_diverse_garland(n, s)
    print(len(diverse_garland))
    print("".join(diverse_garland))

if __name__ == "__main__":
    main()

