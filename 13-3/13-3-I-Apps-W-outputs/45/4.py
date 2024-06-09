
def get_min_knights_to_remove(knights, colors, counts):
    # Initialize a dictionary to store the counts of each color
    color_counts = {color: 0 for color in range(1, len(colors) + 1)}
    
    # Iterate through the knights and increment the count of their color
    for knight, color in zip(knights, colors):
        color_counts[color] += 1
    
    # Initialize the minimum number of knights to remove to be the total number of knights
    min_knights_to_remove = len(knights)
    
    # Iterate through the possible starting indices
    for start_index in range(len(knights)):
        # Initialize the current count of each color to be the count at the starting index
        current_counts = {color: color_counts[color] for color in range(1, len(colors) + 1)}
        
        # Iterate through the knights after the starting index
        for knight, color in zip(knights[start_index:], colors[start_index:]):
            # Decrement the count of the current color
            current_counts[color] -= 1
            
            # If the current count is less than the desired count, break the loop
            if current_counts[color] < counts[color - 1]:
                break
            
            # If the current count is equal to the desired count, check if it is the minimum number of knights to remove
            if current_counts[color] == counts[color - 1]:
                # Calculate the number of knights to remove
                num_knights_to_remove = len(knights) - start_index - 1
                
                # If the number of knights to remove is less than the minimum, update the minimum
                if num_knights_to_remove < min_knights_to_remove:
                    min_knights_to_remove = num_knights_to_remove
    
    # If the minimum number of knights to remove is the total number of knights, it is not possible to select the desired interval
    if min_knights_to_remove == len(knights):
        return -1
    
    # Otherwise, return the minimum number of knights to remove
    return min_knights_to_remove

if __name__ == '__main__':
    knights = [3, 3, 1, 2, 2, 1, 1, 3]
    colors = [3, 3, 1, 2, 2, 1, 1, 3]
    counts = [3, 1, 1]
    print(get_min_knights_to_remove(knights, colors, counts))

