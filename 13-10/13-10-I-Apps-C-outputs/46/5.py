
def get_proclamations(starting_sequence, resulting_sequence, N):
    # Initialize a list to store the proclamations
    proclamations = []
    
    # Loop through the resulting sequence and check if the frog with the current ID is in the correct position
    for i in range(N):
        # If the frog is not in the correct position, find the correct position and add the proclamation to the list
        if resulting_sequence[i] != starting_sequence[i]:
            # Find the correct position of the frog
            correct_position = resulting_sequence.index(starting_sequence[i])
            # Add the proclamation to the list
            proclamations.append(correct_position)
    
    # Return the list of proclamations
    return proclamations

def main():
    # Read the input
    N = int(input())
    starting_sequence = list(map(int, input().split()))
    resulting_sequence = list(map(int, input().split()))
    
    # Call the get_proclamations function and print the result
    proclamations = get_proclamations(starting_sequence, resulting_sequence, N)
    print(*proclamations)

if __name__ == '__main__':
    main()

