
def get_color_choices(n, k):
    # Initialize a list to store the color choices
    color_choices = []
    
    # Iterate through the pairs
    for i in range(n):
        # Choose a color for the man's costume
        man_color = i % k + 1
        
        # Choose a color for the woman's costume
        woman_color = (i + 1) % k + 1
        
        # Make sure the colors are different
        while woman_color == man_color:
            woman_color = (woman_color + 1) % k + 1
        
        # Add the color choices to the list
        color_choices.append((man_color, woman_color))
    
    return color_choices

def check_color_choices(n, k, color_choices):
    # Check if there are any identical pairs
    for i in range(n):
        for j in range(i + 1, n):
            if color_choices[i] == color_choices[j]:
                return False
    
    # Check if there are any pairs with the same color
    for i in range(n):
        if color_choices[i][0] == color_choices[i][1]:
            return False
    
    # Check if there are any consecutive pairs with the same color
    for i in range(n - 1):
        if color_choices[i][0] == color_choices[i + 1][0] or color_choices[i][1] == color_choices[i + 1][1]:
            return False
    
    return True

def main():
    n, k = map(int, input().split())
    color_choices = get_color_choices(n, k)
    if check_color_choices(n, k, color_choices):
        print("YES")
        for man_color, woman_color in color_choices:
            print(man_color, woman_color)
    else:
        print("NO")

if __name__ == '__main__':
    main()

