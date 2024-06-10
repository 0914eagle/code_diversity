
def get_number_of_arrangements(n_colors, balls_per_color, colors_not_next_to_each_other, favorite_sequence):
    # Initialize a counter for the number of arrangements
    num_arrangements = 0
    
    # Iterate over all possible arrangements of the balls
    for arrangement in itertools.permutations(range(1, n_colors+1)):
        # Check if the arrangement satisfies the conditions
        if check_arrangement(arrangement, balls_per_color, colors_not_next_to_each_other, favorite_sequence):
            # If the arrangement satisfies the conditions, increment the counter
            num_arrangements += 1
    
    # Return the number of arrangements modulo 1000000007
    return num_arrangements % 1000000007

def check_arrangement(arrangement, balls_per_color, colors_not_next_to_each_other, favorite_sequence):
    # Initialize a counter for the number of occurrences of the favorite sequence
    num_occurrences = 0
    
    # Iterate over the colors in the arrangement
    for i in range(len(arrangement)):
        # Check if the current color is one of the colors not allowed to be next to each other
        if arrangement[i] in colors_not_next_to_each_other:
            # If it is, return False immediately
            return False
        
        # Check if the current color is the first color in the favorite sequence
        if arrangement[i] == favorite_sequence[0]:
            # If it is, increment the counter for the number of occurrences of the favorite sequence
            num_occurrences += 1
    
    # Return True if the number of occurrences of the favorite sequence is at least as many as the number of balls of the first color in the favorite sequence
    return num_occurrences >= balls_per_color[favorite_sequence[0] - 1]

if __name__ == '__main__':
    n_colors = int(input())
    balls_per_color = list(map(int, input().split()))
    colors_not_next_to_each_other = list(map(int, input().split()))
    favorite_sequence = list(map(int, input().split()))
    print(get_number_of_arrangements(n_colors, balls_per_color, colors_not_next_to_each_other, favorite_sequence))

