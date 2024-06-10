
def get_max_executives(num_briefcases, briefcase_contents):
    # Sort the briefcase contents in non-decreasing order
    briefcase_contents.sort()
    # Initialize the maximum number of executives to be rewarded as 0
    max_executives = 0
    # Initialize the total number of bananas to be 0
    total_bananas = 0
    # Iterate through the sorted briefcase contents
    for briefcase in briefcase_contents:
        # If the total number of bananas plus the number of bananas in the current briefcase is less than or equal to the number of briefcases,
        # increment the maximum number of executives to be rewarded and add the number of bananas in the current briefcase to the total
        if total_bananas + briefcase <= num_briefcases:
            max_executives += 1
            total_bananas += briefcase
    # Return the maximum number of executives that can be rewarded
    return max_executives

def main():
    num_briefcases = int(input())
    briefcase_contents = list(map(int, input().split()))
    print(get_max_executives(num_briefcases, briefcase_contents))

if __name__ == '__main__':
    main()

