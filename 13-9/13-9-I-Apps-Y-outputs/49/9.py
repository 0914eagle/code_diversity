
def solve(s):
    # Convert the input string to a list of digits
    digits = [int(digit) for digit in s]
    # Initialize a variable to store the maximum number of divisible numbers
    max_divisible_numbers = 0
    # Loop through each possible number of cuts
    for cuts in range(len(digits)):
        # Initialize a variable to store the current number of divisible numbers
        divisible_numbers = 0
        # Loop through each possible combination of cuts
        for cut_positions in itertools.combinations(range(1, len(digits)), cuts):
            # Add the current number of divisible numbers for this combination of cuts
            divisible_numbers += sum(1 for i in range(len(cut_positions)) if digits[cut_positions[i]] % 3 == 0)
        # Update the maximum number of divisible numbers if necessary
        max_divisible_numbers = max(max_divisible_numbers, divisible_numbers)
    # Return the maximum number of divisible numbers
    return max_divisible_numbers

