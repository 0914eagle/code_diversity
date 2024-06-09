
def print_round(lines, delay):
    # Initialize variables
    line_1 = []
    line_2 = []
    time_1 = 0
    time_2 = delay

    # Iterate through each line of the input
    for line in lines:
        # Split the line into syllables and time allocations
        syllables = line.split()
        times = [int(time) for time in syllables[1:]]

        # Add the syllables to the appropriate line
        for i, syllable in enumerate(syllables[:1]):
            if time_1 < time_2:
                line_1.append(syllable)
                time_1 += times[i]
            else:
                line_2.append(syllable)
                time_2 += times[i]

    # Print the lines
    print("_".join(line_1))
    print("_".join(line_2))

# Test the function with the sample input
lines = ["Hot cross buns! = Hot cross buns! =", "4 4 4 4 4 4 4 4", "One a pen- ny, Two a pen- ny, Hot cross buns! =", "2 2 2 2 2 2 2 2 4 4 4 4"]
delay = 16
print_round(lines, delay)

