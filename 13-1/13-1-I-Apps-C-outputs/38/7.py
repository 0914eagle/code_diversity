
def print_round(lines, delay):
    # Initialize variables
    line_count = len(lines)
    max_syllables = 80
    max_time = 128
    output = []

    # Iterate over each line of the input
    for i in range(line_count):
        # Get the syllables and time allocation for the first voice
        first_voice = lines[i * 2].split()
        first_time = [int(x) for x in lines[i * 2 + 1].split()]

        # Get the syllables and time allocation for the second voice
        second_voice = lines[i * 2 + 2].split()
        second_time = [int(x) for x in lines[i * 2 + 3].split()]

        # Initialize the output for this line
        output_line = []

        # Iterate over each syllable in the first voice
        for j in range(len(first_voice)):
            # Get the syllable and time allocation for this syllable
            syllable = first_voice[j]
            time = first_time[j]

            # Add the syllable to the output
            output_line.append(syllable)

            # Check if there is a syllable in the second voice that starts at the same time
            if j < len(second_voice) and second_time[j] == time:
                # Add the syllable from the second voice to the output
                output_line.append(second_voice[j])

        # Add the output line to the overall output
        output.append("_".join(output_line))

    # Return the output
    return "\n".join(output)

