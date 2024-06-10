
def get_proclamations(starting_sequence, resulting_sequence, max_proclamations=100000):
    
    n = len(starting_sequence)
    proclamations = []
    while starting_sequence != resulting_sequence:
        # Find the position of the frog with the ID of the minimum element in the resulting sequence
        min_element = min(resulting_sequence)
        min_element_index = resulting_sequence.index(min_element)
        # Find the position of the frog with the ID of the minimum element in the starting sequence
        min_element_starting_index = starting_sequence.index(min_element)
        # Calculate the number of leaps needed to move the frog with the minimum element to its desired position
        leaps_needed = (min_element_index - min_element_starting_index) % n
        # Add the number of leaps needed to the sequence of proclamations
        proclamations.append(leaps_needed)
        # Update the starting sequence by performing the leaps
        starting_sequence = starting_sequence[leaps_needed:] + starting_sequence[:leaps_needed]
        # Update the resulting sequence by swapping the frog with the minimum element with the frog at its desired position
        resulting_sequence = resulting_sequence[:min_element_index] + resulting_sequence[min_element_index + 1:] + [resulting_sequence[min_element_index]]
    return proclamations

def main():
    n = int(input())
    starting_sequence = list(map(int, input().split()))
    resulting_sequence = list(map(int, input().split()))
    proclamations = get_proclamations(starting_sequence, resulting_sequence)
    print(*proclamations)

if __name__ == '__main__':
    main()

