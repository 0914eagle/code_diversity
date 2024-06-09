
def print_round(lines, delay):
    # Initialize variables
    line_count = len(lines)
    max_syllables = 80
    max_time = 128
    output = []

    # Iterate through each line of the input
    for i in range(line_count):
        # Get the syllables and time allocation for the first voice
        first_voice = lines[i * 2].split()
        first_time = [int(x) for x in lines[i * 2 + 1].split()]

        # Get the syllables and time allocation for the second voice
        second_voice = lines[i * 2 + 2].split()
        second_time = [int(x) for x in lines[i * 2 + 3].split()]

        # Initialize the output for the first voice
        first_output = ""
        for j in range(len(first_voice)):
            first_output += first_voice[j]
            if j < len(first_voice) - 1:
                first_output += "_"

        # Initialize the output for the second voice
        second_output = ""
        for j in range(len(second_voice)):
            second_output += second_voice[j]
            if j < len(second_voice) - 1:
                second_output += "_"

        # Iterate through each syllable of the first voice
        for j in range(len(first_voice)):
            # Get the time allocated to the current syllable
            current_time = first_time[j]

            # Check if the current syllable is started by the second voice
            if current_time + delay in second_time:
                # Get the index of the syllable in the second voice that is started at the current time
                index = second_time.index(current_time + delay)

                # Add the syllable to the output for the second voice
                second_output = second_output[:index * (max_syllables + 1)] + second_voice[index] + second_output[index * (max_syllables + 1) + 1:]

        # Add the output for the first and second voice to the overall output
        output.append(first_output)
        output.append(second_output)

    return output

