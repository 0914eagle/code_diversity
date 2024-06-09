
def max_divisible_by_3(s):
    # Initialize a variable to store the maximum number of numbers divisible by 3
    max_count = 0
    # Loop through each possible cut
    for i in range(len(s)):
        # Split the number into two parts
        part1, part2 = s[:i], s[i:]
        # Check if both parts are divisible by 3
        if part1 % 3 == 0 and part2 % 3 == 0:
            # Increment the maximum count
            max_count += 1
    # Return the maximum count
    return max_count

