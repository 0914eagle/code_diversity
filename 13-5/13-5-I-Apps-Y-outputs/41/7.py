
def get_color_choices(n, k):
    # Initialize a list to store the color choices
    color_choices = []
    
    # Iterate through the pairs
    for i in range(n):
        # Choose a color for the man's costume
        man_color = i % k + 1
        
        # Choose a color for the woman's costume that is different from the man's color
        woman_color = (i + 1) % k + 1
        while woman_color == man_color:
            woman_color = (i + 2) % k + 1
        
        # Add the color choices to the list
        color_choices.append((man_color, woman_color))
    
    return color_choices

def check_color_choices(color_choices, n, k):
    # Check if there are any duplicate pairs
    for i in range(n):
        for j in range(i + 1, n):
            if color_choices[i] == color_choices[j]:
                return False
    
    # Check if there are any pairs with the same color
    for i in range(n):
        if color_choices[i][0] == color_choices[i][1]:
            return False
    
    # Check if there are any two consecutive pairs with the same color
    for i in range(n - 1):
        if color_choices[i][0] == color_choices[i + 1][0] or color_choices[i][1] == color_choices[i + 1][1]:
            return False
    
    return True

def main():
    n, k = map(int, input().split())
    color_choices = get_color_choices(n, k)
    if check_color_choices(color_choices, n, k):
        print("YES")
        for man_color, woman_color in color_choices:
            print(man_color, woman_color)
    else:
        print("NO")

if __name__ == '__main__':
    main()

