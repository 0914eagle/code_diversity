
def get_maximum_number_of_executives(briefcase_numbers):
    
    # Sort the briefcase numbers in descending order
    briefcase_numbers.sort(reverse=True)
    
    # Initialize variables to keep track of the number of executives and the total number of bananas
    num_executives = 0
    total_bananas = 0
    
    # Loop through the briefcase numbers and assign them to the executives in a fair way
    for i, briefcase_number in enumerate(briefcase_numbers):
        # If the current briefcase number is greater than the total number of bananas, break the loop
        if briefcase_number > total_bananas:
            break
        
        # Assign the current briefcase number to the current executive
        total_bananas += briefcase_number
        num_executives += 1
    
    # Return the maximum number of executives that can be rewarded
    return num_executives

def main():
    # Read the number of briefcases and their numbers from stdin
    num_briefcases = int(input())
    briefcase_numbers = list(map(int, input().split()))
    
    # Call the get_maximum_number_of_executives function and print the result
    print(get_maximum_number_of_executives(briefcase_numbers))

if __name__ == '__main__':
    main()

