
def get_diverse_garland(n, s):
    # Initialize variables
    recolored_lamp_count = 0
    diverse_garland = []
    current_color = s[0]
    diverse_garland.append(current_color)
    
    # Iterate through the garland
    for i in range(1, n):
        # If the current lamp is not the same color as the previous lamp, add it to the diverse garland
        if s[i] != current_color:
            diverse_garland.append(s[i])
            current_color = s[i]
            recolored_lamp_count += 1
        # If the current lamp is the same color as the previous lamp, recolor it and add it to the diverse garland
        else:
            diverse_garland.append(get_new_color(current_color))
            recolored_lamp_count += 1
    
    return recolored_lamp_count, "".join(diverse_garland)

def get_new_color(color):
    if color == "R":
        return "G"
    elif color == "G":
        return "B"
    else:
        return "R"

if __name__ == '__main__':
    n = int(input())
    s = input()
    recolored_lamp_count, diverse_garland = get_diverse_garland(n, s)
    print(recolored_lamp_count)
    print(diverse_garland)

