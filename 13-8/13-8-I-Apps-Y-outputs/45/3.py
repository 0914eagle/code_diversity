
def get_diverse_garland(n, s):
    # Initialize variables
    recolored_lamp = 0
    diverse_garland = []
    
    # Iterate through the garland
    for i in range(n):
        # If the current lamp is not the same as the next lamp, add it to the diverse garland
        if s[i] != s[(i+1)%n]:
            diverse_garland.append(s[i])
        # If the current lamp is the same as the next lamp, recolor it and add it to the diverse garland
        else:
            recolored_lamp += 1
            diverse_garland.append(s[(i+1)%n])
    
    return recolored_lamp, "".join(diverse_garland)

def main():
    n = int(input())
    s = input()
    recolored_lamp, diverse_garland = get_diverse_garland(n, s)
    print(recolored_lamp)
    print(diverse_garland)

if __name__ == '__main__':
    main()

