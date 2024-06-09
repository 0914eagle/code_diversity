
def get_color_choices(n, k):
    # Initialize a list to store the color choices
    color_choices = []
    
    # Iterate through each pair
    for i in range(n):
        # Get the current pair's color choices
        b, g = get_pair_color_choices(i, k)
        
        # Add the color choices to the list
        color_choices.append((b, g))
    
    # Return the list of color choices
    return color_choices

def get_pair_color_choices(i, k):
    # Get the current pair's index
    current_pair = i + 1
    
    # Get the previous pair's index
    previous_pair = current_pair - 1 if current_pair > 1 else n
    
    # Get the next pair's index
    next_pair = current_pair + 1 if current_pair < n else 1
    
    # Get the previous pair's man's color
    previous_man_color = color_choices[previous_pair - 1][0]
    
    # Get the previous pair's woman's color
    previous_woman_color = color_choices[previous_pair - 1][1]
    
    # Get the next pair's man's color
    next_man_color = color_choices[next_pair - 1][0]
    
    # Get the next pair's woman's color
    next_woman_color = color_choices[next_pair - 1][1]
    
    # Initialize the current pair's man's color to 0
    current_man_color = 0
    
    # Initialize the current pair's woman's color to 0
    current_woman_color = 0
    
    # If the current pair is not the first pair
    if current_pair > 1:
        # If the previous pair's man's color is not the same as the current pair's man's color
        if previous_man_color != current_man_color:
            # Set the current pair's man's color to the previous pair's man's color
            current_man_color = previous_man_color
        # If the previous pair's woman's color is not the same as the current pair's woman's color
        if previous_woman_color != current_woman_color:
            # Set the current pair's woman's color to the previous pair's woman's color
            current_woman_color = previous_woman_color
    
    # If the current pair is not the last pair
    if current_pair < n:
        # If the next pair's man's color is not the same as the current pair's man's color
        if next_man_color != current_man_color:
            # Set the current pair's man's color to the next pair's man's color
            current_man_color = next_man_color
        # If the next pair's woman's color is not the same as the current pair's woman's color
        if next_woman_color != current_woman_color:
            # Set the current pair's woman's color to the next pair's woman's color
            current_woman_color = next_woman_color
    
    # Return the current pair's man's color and woman's color
    return current_man_color, current_woman_color

if __name__ == '__main__':
    # Get the number of pairs and the number of colors
    n, k = map(int, input().split())
    
    # Get the color choices for each pair
    color_choices = get_color_choices(n, k)
    
    # Print the color choices for each pair
    for i in range(n):
        print(color_choices[i][0], color_choices[i][1])

