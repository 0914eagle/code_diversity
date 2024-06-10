
def get_colors(n):
    return list(map(int, input().split()))

def get_condition(k):
    return list(map(int, input().split()))

def get_sequence(l):
    return list(map(int, input().split()))

def count_arrangements(colors, condition, sequence):
    # Initialize the number of arrangements to 0
    arrangements = 0
    
    # Iterate over each color in the sequence
    for i in range(len(sequence)):
        # Check if the current color is in the condition
        if sequence[i] in condition:
            # If it is, then find the index of the next color in the sequence
            next_index = sequence.index(sequence[(i + 1) % len(sequence)])
            # Find the index of the current color in the colors list
            current_index = colors.index(sequence[i])
            # Calculate the number of available positions for the current color
            available_positions = len(colors) - next_index + current_index
            # Calculate the number of arrangements for the current color
            arrangements += available_positions * count_arrangements(colors[next_index:], condition, sequence[i + 1:])
    
    # If the sequence is empty, then return 1 arrangement
    if not sequence:
        return 1
    
    # Return the number of arrangements
    return arrangements

def main():
    # Get the number of colors
    n = int(input())
    # Get the colors
    colors = get_colors(n)
    # Get the condition
    k = int(input())
    condition = get_condition(k)
    # Get the sequence
    l = int(input())
    sequence = get_sequence(l)
    # Calculate the number of arrangements
    arrangements = count_arrangements(colors, condition, sequence)
    # Print the number of arrangements
    print(arrangements % 1000000007)

if __name__ == '__main__':
    main()

