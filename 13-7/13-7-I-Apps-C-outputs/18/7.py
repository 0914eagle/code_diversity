
def get_maximum_number_of_executives(number_of_briefcases, briefcase_contents):
    # Sort the briefcase contents in descending order
    sorted_briefcase_contents = sorted(briefcase_contents, reverse=True)

    # Initialize the number of executives to be rewarded
    number_of_executives = 0

    # Loop through the sorted briefcase contents
    for i in range(len(sorted_briefcase_contents)):
        # If the current briefcase content is greater than or equal to the total number of executives,
        # then add one executive and break the loop
        if sorted_briefcase_contents[i] >= number_of_executives:
            number_of_executives += 1
            break

    return number_of_executives

def get_executive_rewards(number_of_executives, briefcase_contents):
    # Initialize the executive rewards
    executive_rewards = [0] * number_of_executives

    # Loop through the briefcase contents
    for i in range(len(briefcase_contents)):
        # If the current briefcase content is greater than or equal to the total number of executives,
        # then add one executive and break the loop
        if briefcase_contents[i] >= number_of_executives:
            executive_rewards[number_of_executives - 1] += 1
            break
        # Otherwise, add the current briefcase content to the current executive's reward
        else:
            executive_rewards[i] += briefcase_contents[i]

    return executive_rewards

def main():
    # Read the number of briefcases and the briefcase contents
    number_of_briefcases = int(input())
    briefcase_contents = list(map(int, input().split()))

    # Get the maximum number of executives that can be rewarded
    number_of_executives = get_maximum_number_of_executives(number_of_briefcases, briefcase_contents)

    # Get the executive rewards
    executive_rewards = get_executive_rewards(number_of_executives, briefcase_contents)

    # Print the maximum number of executives that can be rewarded
    print(number_of_executives)

    # Print the executive rewards
    for i in range(number_of_executives):
        print(executive_rewards[i])

if __name__ == '__main__':
    main()

