
def get_diverse_garland(n, s):
    # Initialize variables
    recolored_lamps = 0
    diverse_garland = []
    current_color = s[0]

    # Iterate through the garland
    for i in range(n):
        # If the current lamp is not the same as the previous lamp, add it to the diverse garland
        if s[i] != current_color:
            diverse_garland.append(s[i])
            current_color = s[i]
            recolored_lamps += 1
        # If the current lamp is the same as the previous lamp, add it to the diverse garland and change its color
        else:
            diverse_garland.append(current_color)
            current_color = "R" if current_color == "G" else "G"
            recolored_lamps += 1

    return recolored_lamps, "".join(diverse_garland)

def main():
    n = int(input())
    s = input()
    recolored_lamps, diverse_garland = get_diverse_garland(n, s)
    print(recolored_lamps)
    print(diverse_garland)

if __name__ == '__main__':
    main()

