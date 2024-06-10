
def get_maximum_executives(briefcase_count, briefcase_contents):
    # Sort the briefcase contents in descending order
    briefcase_contents.sort(reverse=True)
    # Initialize the number of executives to be rewarded
    executives_rewarded = 0
    # Initialize the total number of bananas rewarded
    total_bananas_rewarded = 0
    # Loop through the briefcase contents
    for briefcase in briefcase_contents:
        # If the total number of bananas rewarded plus the current briefcase is less than or equal to the total number of bananas in all the briefcases,
        # then reward the executive with the current briefcase and update the number of executives rewarded and the total number of bananas rewarded
        if total_bananas_rewarded + briefcase <= sum(briefcase_contents):
            executives_rewarded += 1
            total_bananas_rewarded += briefcase
    # Return the maximum number of executives that can be rewarded
    return executives_rewarded

def main():
    # Read the number of briefcases and their contents from stdin
    briefcase_count = int(input())
    briefcase_contents = list(map(int, input().split()))
    # Call the get_maximum_executives function and print the result
    print(get_maximum_executives(briefcase_count, briefcase_contents))

if __name__ == '__main__':
    main()

