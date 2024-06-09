
def solve(notes):
    # Sort the notes in ascending order
    sorted_notes = sorted(notes)

    # Initialize variables to keep track of the maximum sum of lengths
    max_sum = 0
    max_subsequence1 = []
    max_subsequence2 = []

    # Iterate over the sorted notes
    for i in range(len(sorted_notes)):
        # Check if the current note is congruent to the previous note modulo 7
        if i > 0 and sorted_notes[i] % 7 == sorted_notes[i-1] % 7:
            # If the current note is congruent to the previous note modulo 7, then it forms a melody with the previous note
            # Add the current note to the first subsequence
            max_subsequence1.append(sorted_notes[i])
            # Add the previous note to the second subsequence
            max_subsequence2.append(sorted_notes[i-1])
            # Calculate the sum of lengths of the two subsequences
            sum_of_lengths = len(max_subsequence1) + len(max_subsequence2)
            # Check if the sum of lengths is greater than the current maximum
            if sum_of_lengths > max_sum:
                # If the sum of lengths is greater than the current maximum, then update the maximum sum and the two subsequences
                max_sum = sum_of_lengths
                max_subsequence1 = max_subsequence1[:]
                max_subsequence2 = max_subsequence2[:]
        else:
            # If the current note is not congruent to the previous note modulo 7, then it is the start of a new subsequence
            # Add the current note to the first subsequence
            max_subsequence1 = [sorted_notes[i]]
            # Clear the second subsequence
            max_subsequence2 = []

    # Return the maximum sum of lengths of the two subsequences
    return max_sum

