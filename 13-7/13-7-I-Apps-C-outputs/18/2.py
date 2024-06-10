
def get_max_executives(briefcase_nums):
    # Sort the briefcase numbers in non-decreasing order
    briefcase_nums.sort()
    # Initialize the number of executives to be rewarded as 0
    num_executives = 0
    # Loop through the briefcase numbers
    for i in range(len(briefcase_nums)):
        # If the current briefcase number is less than or equal to the number of bananas in the previous briefcase number, continue to the next iteration
        if briefcase_nums[i] <= briefcase_nums[i-1]:
            continue
        # Otherwise, increment the number of executives to be rewarded
        num_executives += 1
    # Return the maximum number of executives that can be rewarded
    return num_executives

def main():
    # Read the number of briefcases and their contents from stdin
    num_briefcases = int(input())
    briefcase_nums = list(map(int, input().split()))
    # Call the get_max_executives function and print the result
    print(get_max_executives(briefcase_nums))

if __name__ == '__main__':
    main()

