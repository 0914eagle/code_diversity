
def polycarp_and_divisibility(s):
    # Convert the input string to a list of integers
    num_list = [int(i) for i in s]
    # Initialize a variable to store the maximum number of divisible numbers
    max_divisible = 0
    # Loop through all possible combinations of cutting the number
    for i in range(len(num_list)):
        # Get the current number by joining the digits between the current and previous cuts
        current_num = int("".join(map(str, num_list[:i])))
        # Check if the current number is divisible by 3
        if current_num % 3 == 0:
            max_divisible += 1
    return max_divisible

